import data_cleaning
import database_utils

# Cleaning data
user_data = data_cleaning.DataCleaning().clean_user_data()
card_payment_data = data_cleaning.DataCleaning().clean_card_data()


# Uploading data to Pgadmin
upload_user_data = database_utils.DatabaseConnector().upload_to_db(panda_df=user_data, table_name='dim_users')
upload_payment_data = database_utils.DatabaseConnector().upload_to_db(panda_df=card_payment_data, table_name='dim_card_details')



