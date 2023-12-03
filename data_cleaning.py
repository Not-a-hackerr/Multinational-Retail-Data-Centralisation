import data_extraction 
import database_utils
import pandas as pd
import re
from dateutil.parser import parse


class DataCleaning:

    def clean_orders_data(self):
        orders_engine = database_utils.DatabaseConnector().init_db_engine()
        orders_data = data_extraction.DataExtractor().read_rds_engine(f"{database_utils.DatabaseConnector().list_db_tables()[2]}", orders_engine)
        
        # Remove NULL columns 
        orders_data = orders_data.drop("first_name", axis=1)
        orders_data = orders_data.drop("last_name", axis=1)
        orders_data = orders_data.drop("1", axis=1)
        orders_data.dropna(inplace=True)
        
        # Card Number
        orders_data["card_number"] = orders_data["card_number"].astype("str")



        # Index 
        orders_data.drop("level_0", axis=1, inplace= True)
        orders_data.drop("index", axis=1, inplace=True)
        orders_data.reset_index(drop=True)

        return orders_data
    

    def convert_product_weights (self, weight_str):
        regex_match = re.match(r'([\d.]+)\s*([a-zA-Z]+)', weight_str)
        
        if regex_match:
            value, unit = regex_match.groups()

            # Convert ml and g to kg
            if unit.lower() == 'ml' or unit.lower() == 'g':
                value = float(value) / 1000  # Convert ml and g to kg

            return float(value)
        else:
            # Remove 'kg' and convert to float
            return float(weight_str.replace('kg', ''))
    

    def clean_product_data(self):
        product_data = data_extraction.DataExtractor().extract_from_s3("s3://data-handling-public/products.csv")
        product_data = product_data.dropna()
         # Removed
        product_data["removed"].value_counts()
        product_data = product_data[product_data["removed"].str.contains("Still_avaliable|Removed")]

        # Category
        product_data["category"].value_counts()

        # EAN
        product_data["EAN"] = pd.to_numeric(product_data["EAN"], errors="coerce")
        product_data.dropna()
        product_data["EAN"] = product_data["EAN"].astype('int64')

        # Weight transfer
        product_data["weight"] = product_data["weight"].apply(self.convert_product_weights)

        # Price
        product_data["product_price"] = product_data["product_price"].str.replace("£", '')
        product_data["product_price"] = product_data["product_price"].astype('float64')

        # Date added
        product_data["date_added"] = product_data["date_added"].apply(parse)
        product_data["date_added"] = pd.to_datetime(product_data["date_added"], infer_datetime_format=True, errors='coerce')

        # Index
        product_data = product_data.drop("Unnamed: 0", axis=1)
        product_data.reset_index(drop=True, inplace=True)

        return product_data
    

    def clean_date_events(self):
        date_events = data_extraction.DataExtractor().retrieve_date_events_data()
        date_events = date_events.dropna()

        # Time period cleaning
        date_events = date_events[date_events["time_period"].str.contains("Evening|Midday|Morning|Late_Hours")]


        date_events.reset_index(drop=True, inplace=True)

        return date_events

    def clean_card_data(self):
        card_payment_data = data_extraction.DataExtractor().retrieve_pdf_data()
        card_payment_data = card_payment_data[["card_number", "expiry_date", "card_provider", "date_payment_confirmed"]]

        # # Cleans card number of null values 
        card_payment_data.card_number = card_payment_data.card_number.astype('str')
        card_payment_data["card_number"] = card_payment_data["card_number"].str.replace('?','')
        card_payment_data = card_payment_data[card_payment_data["card_number"].str.isnumeric()]
      
        # Cleans and convert date_payment_confirmed
        card_payment_data["date_payment_confirmed"] = card_payment_data["date_payment_confirmed"].apply(parse)
        card_payment_data["date_payment_confirmed"] = pd.to_datetime(card_payment_data["date_payment_confirmed"], infer_datetime_format=True, errors='coerce')

        # Corrects the index column
        card_payment_data = card_payment_data.reset_index(drop=True)

        return card_payment_data
    

    def clean_store_data(self):
        # store_data = data_extraction.DataExtractor().retrieve_stores_data()
        store_data = pd.read_csv("store_data.csv")

        store_data = store_data.drop("lat", axis=1)

        # store_type
        '''
        Cleaning a column which has a few distinct values first is the best and easiest to clear
        other rows with errors
        '''
        store_data["store_type"].unique()
        valid_values = ['Web Portal', 'Local', 'Super Store', 'Mall Kiosk', 'Outlet']
        store_data = store_data[store_data["store_type"].isin(valid_values)]

        # cleans Staff numbers
        store_data["staff_numbers"] = store_data["staff_numbers"].str.replace(r'\D', '', regex=True)

        # Continent
        store_data["continent"].value_counts()
        store_data["continent"] = store_data["continent"].replace({"eeEurope": "Europe", "eeAmerica":"America"}) 

        # Opening_date
        store_data["opening_date"] = store_data["opening_date"].apply(parse)
        store_data["opening_date"] = pd.to_datetime(store_data["opening_date"], infer_datetime_format=True, errors='coerce')
        
        # # Resetting the index
        store_data.drop("index", axis=1, inplace=True)
        store_data.drop("Unnamed: 0", axis=1, inplace=True)
        store_data.reset_index(inplace=True, drop=True)

        return store_data
    
    def clean_user_data(self):
        engine = database_utils.DatabaseConnector().init_db_engine()
        user_data = data_extraction.DataExtractor().read_rds_engine("legacy_users", engine)
        
        # Find and clear Null values in first and last names
        user_data = user_data[~user_data["first_name"].str.contains('null',case=False) | user_data["last_name"].str.contains('null',case=False)]

        # Checking and cleaning country for out of place values
        """ 
        user_data["country"].value_counts(), Gives the sum on each unique item in the column
        The below code only includes data entries with United Kingdom OR Germany ORUnited States in the column
        """
        user_data = user_data[user_data["country"].str.contains('United Kingdom|Germany|United States')]

        # Cleaning country code
        # user_data["country_code"].unique()
        user_data["country_code"].replace({'GGB' : 'GB' }, inplace=True)

        # Checking of DOB and join_date
        user_data["date_of_birth"] = user_data["date_of_birth"].apply(parse)
        user_data["date_of_birth"] = pd.to_datetime(user_data["date_of_birth"], infer_datetime_format=True, errors='coerce')

        user_data["join_date"] = user_data["join_date"].apply(parse)
        user_data["join_date"] = pd.to_datetime(user_data["join_date"], infer_datetime_format=True, errors='coerce')

        # Remove extra index column
        user_data.drop("index", axis=1, inplace=True)
        user_data.reset_index(drop=True, inplace=True)

        return user_data

