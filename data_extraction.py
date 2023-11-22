import tabula
import pandas as pd

class DataExtractor:
    def read_rds_engine(self):
        pass
    
    def retrieve_pdf_data(self):
        pdf_path = "https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"
        dfs = tabula.read_pdf(pdf_path, stream=True, pages="1,2,3,4,5,6")
        dfs = pd.concat(dfs)
        return dfs


# DE = DataExtractor()
# card_payment_data = DE.retrieve_pdf_data()
# card_payment_data

