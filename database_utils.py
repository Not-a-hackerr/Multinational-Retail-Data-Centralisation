import yaml
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import inspect
import psycopg2

class DatabaseConnector:
    def read_db_creds(self):
        with open('db_creds.yaml') as f:
            data_base_creds = yaml.load(f, Loader=yaml.FullLoader)
        return data_base_creds
    
    # Reads credentials from read_db_creds dictionay
    def init_db_engine(self):
        db_creds_dict = self.read_db_creds()
        engine = create_engine(f"postgresql://{db_creds_dict['RDS_USER']}:{db_creds_dict['RDS_PASSWORD']}@{db_creds_dict['RDS_HOST']}:{db_creds_dict['RDS_PORT']}/{db_creds_dict['RDS_DATABASE']}")
        engine = engine.connect()
        return engine

    def list_db_tables(self):
        engine = self.init_db_engine()
        inspector = inspect(engine)
        table_names = inspector.get_table_names()
        return table_names

    # Upload data in sales_data db in a table named dim_users
    def upload_to_db(self, panda_df, table_name):
        # Place a try and except condition for only panda DF accepted 
        db_creds_dict = self.read_db_creds()
        db_engine = create_engine(f"postgresql://{db_creds_dict['PG_USER']}:{db_creds_dict['PG_PASSWORD']}@{db_creds_dict['PG_HOST']}/{db_creds_dict['PG_DATABASE']}")
        db_engine = db_engine.connect()

        panda_df.to_sql(f'{table_name}', con=db_engine, if_exists='replace', index=False)


if __name__ == '__main__':
    pass