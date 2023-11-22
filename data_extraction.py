import tabula
import pandas as pd
from dateutil.parser import parse

class DataExtractor:
    def read_rds_engine(self):
        pass
    
    def retrieve_pdf_data(self):
        pdf_path = "https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"
        dfs = tabula.read_pdf(pdf_path, stream=True, pages="all")
        dfs = pd.concat(dfs)
        return dfs


