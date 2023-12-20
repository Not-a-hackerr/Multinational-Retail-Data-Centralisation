import pandas as pd
import data_cleaning
import database_utils
import data_extraction
DU = database_utils.DatabaseConnector()
DC = data_cleaning.DataCleaning()
DE = data_extraction.DataExtractor()


if __name__ == '__main__':
    # Cleaning data
    orders_engine = DU.init_db_engine()
    the_orders_data = DE.read_rds_engine(f"{DU.list_db_tables()[2]}", orders_engine)
    orders_data = DC.clean_orders_data(the_orders_data)

    the_product_data = DE.extract_from_s3("s3://data-handling-public/products.csv")
    product_data = DC.clean_product_data(the_product_data)

    the_date_events = DE.retrieve_date_events_data()
    date_events_data = DC.clean_date_events(the_date_events)

    the_card_payment_data = data_extraction.DataExtractor().retrieve_pdf_data()
    card_payment_data = DC.clean_card_data(the_card_payment_data)

    the_store_data = pd.read_csv("store_data.csv")
    store_data = DC.clean_store_data(the_store_data)

    engine = DU.init_db_engine()
    the_user_data = DE.read_rds_engine("legacy_users", engine)
    user_data = DC.clean_user_data(the_user_data)


    # Uploading data to Pgadmin
    upload_user_data =  DU.upload_to_db(panda_df=user_data, table_name='dim_users')
    upload_payment_data =  DU.upload_to_db(panda_df=card_payment_data, table_name='dim_card_details')
    upload_store_data =  DU.upload_to_db(panda_df=store_data, table_name='dim_store_details')
    upload_product_data =  DU.upload_to_db(panda_df=product_data, table_name='dim_products')
    upload_orders_data =  DU.upload_to_db(panda_df=orders_data, table_name="orders_table")
    upload_date_event_data =  DU.upload_to_db(panda_df=date_events_data,table_name="dim_date_times")
