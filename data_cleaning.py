import pandas as pd
import data_extraction 
from dateutil.parser import parse


class DataCleaning:
    def clean_user_data(self):
        pass

    def clean_card_data(self):
        DE = data_extraction.DataExtractor()
        card_payment_data  = DE.retrieve_pdf_data()
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
card_data = clean.clean_card_data()
card_data





