import data_cleaning
import database_utils

if __name__ == '__main__':
    # Cleaning data
    user_data = data_cleaning.DataCleaning().clean_user_data()
    card_payment_data = data_cleaning.DataCleaning().clean_card_data()
    store_data = data_cleaning.DataCleaning().clean_store_data()
    product_data = data_cleaning.DataCleaning().clean_product_data()
    orders_data = data_cleaning.DataCleaning().clean_orders_data()
    date_events_data = data_cleaning.DataCleaning().clean_date_events()


    # Uploading data to Pgadmin
    upload_user_data = database_utils.DatabaseConnector().upload_to_db(panda_df=user_data, table_name='dim_users')
    upload_payment_data = database_utils.DatabaseConnector().upload_to_db(panda_df=card_payment_data, table_name='dim_card_details')
    upload_store_data = database_utils.DatabaseConnector().upload_to_db(panda_df=store_data, table_name='dim_store_details')
    upload_product_data = database_utils.DatabaseConnector().upload_to_db(panda_df=product_data, table_name='dim_products')
    upload_orders_data = database_utils.DatabaseConnector().upload_to_db(panda_df=orders_data, table_name="orders_table")
    upload_date_event_data = database_utils.DatabaseConnector().upload_to_db(panda_df=date_events_data,table_name="dim_date_times")

