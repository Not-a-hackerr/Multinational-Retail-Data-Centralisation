import tabula
import pandas as pd
import requests
import boto3
from io import StringIO


class DataExtractor:
    def __init__(self):
        self.api_header_deats = {"x-api-key":"yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}

    """
    sqlalchemy helps you connect to cloud services, here we are connecting to a aws cloud to read data
    to then clean it and add it to pgadmin

    Engine is essentially the connection between this local device and the cloud 

    parameter - table_name is a parameter because there are a wind variety of object that table_name could be
    variable - The exact object that is put in for table_name 
    """
    def read_rds_engine(self, table_name, engine):
        with engine as connection:
            data = pd.read_sql_table(f"{table_name}", engine)
        return data
    
    def retrieve_pdf_data(self):
        pdf_path = "https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"
        payment = tabula.read_pdf(pdf_path, stream=True, pages="all")
        payment = pd.concat(payment)
        return payment

    def list_number_of_stores(self):
        response = requests.get("https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores",headers=self.api_header_deats)
        response = response.json()
        number_of_stores = response["number_stores"]
        return number_of_stores
    
    def retrieve_stores_data(self):
        response_list = []
        for i in range(self.list_number_of_stores()):
            response = requests.get(f"https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{i}", headers=self.api_header_deats)
            data = response.json()
            response_list.append(data)
        store_data = pd.DataFrame(response_list)   
        # store_data.to_csv("store_data.csv")
        return store_data
    
    def extract_from_s3(self, s3_address):
        bucket, key = s3_address.replace('s3://', '').split('/', 1)
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket=bucket, Key=key)
        data = response['Body'].read().decode('utf-8')
        data_io = StringIO(data)
        df = pd.read_csv(data_io)
        return df 

        



# DE = DataExtractor()


