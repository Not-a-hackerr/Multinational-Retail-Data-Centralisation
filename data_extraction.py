import pandas as pd
import requests
import tabula
import boto3
from io import StringIO
from database_utils import DatabaseConnector


class DataExtractor:
    '''
    This Class holds all the methods that extract data from their various sources

    Attributes
    self.db_creds_dict: These are credential details which are saved in a YAML file are used to connect to an API
    '''
    def __init__(self):
        self.api_header_deats = DatabaseConnector().read_db_creds()['api_header_deats']
  
    def read_rds_engine(self, table_name, engine):
        '''
        This method reads AWS RDS and converts it into a pandas dataframe

        Method variables
        table name: the name of the table in the RDS the user is attempting to read
        engine: The engine connection used to connect to the RDS
        '''
        data = pd.read_sql_table(f"{table_name}", engine)
        return data
    
    def retrieve_pdf_data(self):
        '''
        This method uses the moduole tabula to read a pdf file and turn it into a pandas dataframe
        '''
        pdf_path = "https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"
        payment = tabula.read_pdf(pdf_path, stream=False, pages="all")
        '''
        Stream = False means when tabula reads the data it assumes there are lines on the pdf and reads the pdf much faster
        '''
        payment = pd.concat(payment)
        return payment

    def list_number_of_stores(self):
        '''
        This method returns the number of stores  
        '''
        response = requests.get("https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores",headers= self.api_header_deats)
        response = response.json()
        number_of_stores = response["number_stores"]
        return number_of_stores
    
    def retrieve_stores_data(self):
        '''
        This method retrieves the store data from AWS 

        Using a for loop, line by line the data is retrieved and appneded to a list
        This list then converted into a pandas dataframe
        '''
        response_list = []
        for i in range(self.list_number_of_stores()):
            response = requests.get(f"https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{i}", headers= self.api_header_deats)
            data = response.json()
            response_list.append(data)
        store_data = pd.DataFrame(response_list)   
        return store_data
    
    def extract_from_s3(self, s3_address):
        '''
        This method allows a user to extract files from an AWS S3 bucket 

        This data needs to be decoded using utf-8 
        It is then converted into a pandas dataframe
        '''
        bucket, key = s3_address.replace('s3://', '').split('/', 1)
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket=bucket, Key=key)
        data = response['Body'].read().decode('utf-8')
        data_io = StringIO(data)
        df = pd.read_csv(data_io)
        return df 

    def retrieve_date_events_data(self):
        '''
        This method retrieves the json data of the date events from AWS S3 and converts it into a pandas dataframe
        '''
        json_path = "https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json"
        date_events = pd.read_json(json_path)
        return date_events
