import yaml
from sqlalchemy import create_engine
from sqlalchemy import inspect


class DatabaseConnector:
    def read_db_creds(self):
        ''''
        This method reads the yaml file that holds all the credentials for the pgadmin connection and the AWS RDS connection
        '''
        with open('db_creds.yaml') as f:
            data_base_creds = yaml.load(f, Loader=yaml.FullLoader)
        return data_base_creds
    
    # Reads credentials from read_db_creds dictiona
    def init_db_engine(self):
        '''
        This method creates and initiates and engine which is the connection to the AWS RDS 
        '''
        db_creds_dict = self.read_db_creds()
        engine = create_engine(f"postgresql://{db_creds_dict['RDS_USER']}:{db_creds_dict['RDS_PASSWORD']}@{db_creds_dict['RDS_HOST']}:{db_creds_dict['RDS_PORT']}/{db_creds_dict['RDS_DATABASE']}")
        engine = engine.connect()
        return engine

    def list_db_tables(self):
        '''
        This method lists the names of the different tables within the database
        '''
        engine = self.init_db_engine()
        inspector = inspect(engine)
        table_names = inspector.get_table_names()
        return table_names

    # Upload data in sales_data db in a table named dim_users
    def upload_to_db(self, panda_df, table_name):
        '''
        This method uploads data to a named database within postgresql

        Class variables
        panda_df: user can specify what pandas df they want to upload
        table_name: here is where the user can specify the postgresql table name
        '''

        # Place a try and except condition for only panda DF accepted 
        db_creds_dict = self.read_db_creds()
        db_engine = create_engine(f"postgresql://{db_creds_dict['PG_USER']}:{db_creds_dict['PG_PASSWORD']}@{db_creds_dict['PG_HOST']}/{db_creds_dict['PG_DATABASE']}")
        db_engine = db_engine.connect()

        panda_df.to_sql(f'{table_name}', con=db_engine, if_exists='replace', index=False)

