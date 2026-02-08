from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
from dotenv import load_dotenv
import os
import json
import pymongo
import sys
import pandas as pd
import numpy as np
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging

load_dotenv()
# Get the URL from your .env file
MONGO_DB_URL = os.getenv("MONGO_DB_URL") 

ca = certifi.where()

class NetworkDataExtract:
    def __init__(self):
        pass

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            # Efficient way to convert DF to List of Dicts
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)   
            
    def insert_data_mongodb(self, records, database_name, collection_name):
        try:
            # Initialize client with SSL certificate
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            
            # Access database and then the collection
            self.db = self.mongo_client[database_name]
            self.coll = self.db[collection_name]
            
            self.coll.insert_many(records)
            return len(records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

if __name__ == '__main__':
    # Use raw string for Windows paths to avoid escape character errors
    FILE_PATH = r"Network_Data\phisingData.csv"
    DATABASE = "HALIM_AI"
    COLLECTION = "Network_Data"    
    
    # FIXED: Initialize the correct class
    network_obj = NetworkDataExtract() 
    
    records = network_obj.csv_to_json_convertor(FILE_PATH)
    print(f"Total records converted: {len(records)}")
    
    no_of_records = network_obj.insert_data_mongodb(records, DATABASE, COLLECTION)
    print(f"Successfully inserted {no_of_records} records.")