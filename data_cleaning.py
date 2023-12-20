import pandas as pd
import re
from dateutil.parser import parse


class DataCleaning:
    '''
    This class is used clean all the data from their respective sources
    '''
    def clean_orders_data(self, orders_data):
        '''
        This method cleans the orders data
        '''
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
        '''
        This method converts the errored entries into one unit kg

        The function accepts one variable named weight_str which is processed by the method below

        The regex code finds all entries that have ml or g as their units,
        this is used as the condition for a conditional statement which then converts g and ml into kg
        by diving them by 1000. All units are then removed and the dtype of the column is converted to a float
        '''
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

    def clean_product_data(self, product_data):
        '''
        This method cleans the product data 

        Firstly drops the all the NaN values
        Then drop all row which dont have either "Still_avaliable" or "Removed" in their removed column 
        The convert_product_weights method is applied in this method to clean the weight column
        'Product_prices' have £ removed and converted to a float
        'Date_added' is converted into a date dtype, pandas also changes all the different date formats into dd-mm-yyyy
        '''
        product_data = product_data.dropna()
        # Removed
        product_data = product_data[product_data["removed"].str.contains("Still_avaliable|Removed")]
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
    

    def clean_date_events(self, date_events):
        '''
        This method cleans the date events data

        If Evening|Midday|Morning|Late_Hours is not in the 'time_period' column the row will be deleted
        '''
        date_events = date_events.dropna()
        # Time period cleaning
        date_events = date_events[date_events["time_period"].str.contains("Evening|Midday|Morning|Late_Hours")]
        date_events.reset_index(drop=True, inplace=True)
        return date_events

    def clean_card_data(self, card_payment_data):
        '''
        This method cleans the card data 

        'date_payment_confirmed' is converted into a date dtype, pandas also changes all the different date formats into dd-mm-yyyy
        '''
        card_payment_data = card_payment_data[["card_number", "expiry_date", "card_provider", "date_payment_confirmed"]]
        # Cleans card number of null values 
        card_payment_data.card_number = card_payment_data.card_number.astype('str')
        card_payment_data["card_number"] = card_payment_data["card_number"].str.replace('?','')
        card_payment_data = card_payment_data[card_payment_data["card_number"].str.isnumeric()]
        # Cleans and convert date_payment_confirmed
        card_payment_data["date_payment_confirmed"] = card_payment_data["date_payment_confirmed"].apply(parse)
        card_payment_data["date_payment_confirmed"] = pd.to_datetime(card_payment_data["date_payment_confirmed"], infer_datetime_format=True, errors='coerce')
        # Corrects the index column
        card_payment_data = card_payment_data.reset_index(drop=True)
        return card_payment_data
    
    def clean_store_data(self, store_data):
        '''
        This method cleans the store data 

        'opening_date' is converted into a date dtype, pandas also changes all the different date formats into dd-mm-yyyy
        '''
        store_data = store_data.drop("lat", axis=1)
        # store_type
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
    
    def clean_user_data(self, user_data):
        '''
        This method cleans the user data

        'opening_date' is converted into a date dtype, pandas also changes all the different date formats into dd-mm-yyyy
        
        '''
        # Find and clear Null values in first and last names
        user_data = user_data[~user_data["first_name"].str.contains('null',case=False) | user_data["last_name"].str.contains('null',case=False)]
        # Checking and cleaning country for out of place values
        user_data = user_data[user_data["country"].str.contains('United Kingdom|Germany|United States')]
        # Cleaning country code
        user_data["country_code"].replace({'GGB' : 'GB'}, inplace=True)
        # Checking of DOB and join_date
        user_data["date_of_birth"] = user_data["date_of_birth"].apply(parse)
        user_data["date_of_birth"] = pd.to_datetime(user_data["date_of_birth"], infer_datetime_format=True, errors='coerce')
        # Converts dates into date dtype
        user_data["join_date"] = user_data["join_date"].apply(parse)
        user_data["join_date"] = pd.to_datetime(user_data["join_date"], infer_datetime_format=True, errors='coerce')
        # Remove extra index column
        user_data.drop("index", axis=1, inplace=True)
        user_data.reset_index(drop=True, inplace=True)
        return user_data
