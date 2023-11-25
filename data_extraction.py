import tabula
import pandas as pd
from fastapi import FastAPI
import requests


class DataExtractor:
    def __init__(self):
        self.api_header_deats = {"x-api-key":"yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}
    """
    sqlalchemy helps you connect to cloud service, here we are connecting to a aws cloud to read data
    to then clean it and add it to pgadmin

    Engine is essentially the connection between this local device and the cloud 

    parameter - table_name is a parameter because there are a wind variety of object that table_name could be
    variable - The exact object that is put in for table_name 
    """
    def read_rds_engine(self, table_name, engine):
        with engine as connection:
            users = pd.read_sql_table(f"{table_name}", engine)
        return users
        
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
        response = requests.get(f"https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{self.list_number_of_stores()}", headers=self.api_header_deats)
        
        return response


DE = DataExtractor()

print(DE.retrieve_stores_data())
    

