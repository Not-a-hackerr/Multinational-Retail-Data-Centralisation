# Multinational Data Centralisation Project 


## Project Description
There is a multinational company which sells various goods around the globe.

Currently, their sales data is spread across various data sources therefore, it is not easily accessible or analysable by current members of the team. 

I have been employed to help this company become more data-driven by collating all data and making it accessible from one centralised location. 

My goals:
- Produce a system that stores the current company data in a database this will act like a source of truth for sales data
- Query the database to get up-to-dte metrics for the business.


## Things learnt in this Project
- Improved my understanding of using OOP within a project 

- Obtain a deeper understanding for cleaning data using pandas

- Extracting data from several data sources
    - pdf
    - S3 buckets 
    - S3 file paths
    - RDS 
    - API
- Creating engines with sqlalchemy to establish connections with an amazon RDS

- Using boto3 to extract data from S3 buckets

## Installation Insructions


## Usage Instructions

## File structure

### database_utils .py
This file contains a class by the name of DatabaseConnecter. This class contains all the database related methods whether that is uploading to pg admin or an initialiser for a database engine.

### data_extraction.py
This file contains a class by the name of DataExtractor. This class contains methods that extract all the data from their respective sources.

### data_cleaning.py
This file contains a class by the name DataCleaning. This class contains methods that cleans all the data from their individual data sources. 

### main.py
This file runs all the methods which clean the data and then uploads it to pgadmin for data analysis.

## Licsense Information