# Multinational Data Centralisation Project 


## Project Description
There is a multinational company which sells various goods around the globe.

Currently, their sales data is spread across various data sources therefore, it is not easily accessible or analysable by current members of the team. 

I have been employed to help this company become more data-driven by collating all data and making it accessible from one centralised location. 

My goals:
- Produce a system that stores the current company data in a database this will act like a source of truth for sales data
- Query the database to get up-to-date metrics for the business


## Things learnt in this Project
- Improved my understanding of using OOP within a project 

- Obtained a deeper understanding for cleaning data using pandas

- Extracting data from several data sources
    - pdf
    - S3 buckets 
    - S3 file paths
    - RDS 
    - API
- Creating engines with sqlalchemy to establish connections with:
    - An amazon RDS
    - PgAdmin for database storge

- Using boto3 to extract data from S3 buckets

- How to query Information within pgadmin using postgresql


## File structure

### Python files

### database_utils .py
This file contains a class by the name of DatabaseConnecter. This class contains all the database related methods whether that is uploading to pgAdmin or a database connector using an engine.

### data_extraction.py
This file contains a class by the name of DataExtractor. This class contains methods that extract all the data from their respective sources.

### data_cleaning.py
This file contains a class by the name of DataCleaning. This class contains methods that clean all the data from their individual data sources. 

### main.py
This file runs all the methods which clean the data and then uploads it to pgAdmin for data analysis.

## SQL Queries

### Casting columns
These queries correctly casts all the data types. 

### Querying
These queries answer key details about the data which is useful for the company:

- How many stores in which countries
- Which locations currently have the most stores
- Months which have produced the largest amount of sales
- How many sales are coming from online
- What percentage of sales come through each type of store
- Which month in each year produced the highest cost of sales
- Staff Headcount in every country
- Which German store is selling the most
- How quickly is the company making sales


## Summary

This project has dramatically improved my confidence and ability in OOP. The new skills I have learnt within postgresql, pandas cleaning and database linkage (boto3, sqlalchemy) has set a foundation from where I can improve upon. 

The hardest part of this project was understanding how to use API's, boto3 and sqlalchemy especially linking to the cloud to extract data. Once everything was set and all connections were established it became easier from there. Using pandas was enjoyable and a stimulating challenge, figuring out the best methods to use to clean the extracted data. Lastly, using postgresql was definitely the most enjoyable part, I was able to build a picture of what the data I extracted and cleaned meant for the business and highlight key areas of improvement. 