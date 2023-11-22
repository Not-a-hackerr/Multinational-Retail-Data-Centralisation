import database_utils
import tabula
import pandas as pd
import inspect
from sqlalchemy import text 
from dateutil.parser import parse

class DataExtractor:
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
        payment = pd.concat(dfs)
        return payment



