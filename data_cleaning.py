import pandas as pd
import data_extraction as DE
from dateutil.parser import parse
import database_utils as DB
import numpy as np

class DataCleaning:

    def clean_user_data(self):
        engine = DB.DatabaseConnector().init_db_engine()
        user_data = DE.DataExtractor().read_rds_engine("legacy_users", engine)
        
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

        # Email address
        email_regular_expression = '^.+@[^\.].*\.[a-z]{2,}$'
        user_data[~user_data["email_address"].str.match(email_regular_expression, 'email_address')] = np.nan 
        user_data = user_data.dropna()
        
        # Phone Number cleaning
        """
        For every row  where the Phone column does not match our regular expression, replace the value with NaN
        (user_data["email_address"].eq('nae')).sum()
        """
        user_data["phone_number"] = user_data["phone_number"].str.replace('x.*$', '', regex=True)
        phone_number_regex = "^(\(?\+?[0-9]*\)?)?[0-9_\- \(\)]*$"
        user_data[~user_data["phone_number"].str.match(phone_number_regex, 'phone_number')] = np.nan
        user_data = user_data.dropna()

        # Remove extra index column
        user_data.drop("index", axis=1, inplace=True)
        user_data.reset_index(drop=True, inplace=True)

        return user_data


    def clean_card_data(self):
        card_payment_data  = DE.DataExtractor().retrieve_pdf_data()
        card_payment_data = card_payment_data[["card_number", "expiry_date", "card_provider", "date_payment_confirmed"]]

        # Cleans card number of null values 
        card_payment_data.card_number = pd.to_numeric(card_payment_data.card_number, errors='coerce')
        card_payment_data = card_payment_data.dropna()
        card_payment_data.card_number = card_payment_data.card_number.astype('int64')

        # Cleans and convert date_payment_confirmed
        card_payment_data["date_payment_confirmed"] = card_payment_data["date_payment_confirmed"].apply(parse)
        card_payment_data["date_payment_confirmed"] = pd.to_datetime(card_payment_data["date_payment_confirmed"], infer_datetime_format=True, errors='coerce')

        # Corrects the index column
        card_payment_data = card_payment_data.reset_index()
        card_payment_data = card_payment_data.drop("index" ,axis=1)

        return card_payment_data


clean = DataCleaning()
# card_data = clean.clean_card_data()
# card_data


clean.clean_user_data()