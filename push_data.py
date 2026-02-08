
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
from dotenv import load_dotenv
import os
import json
import sys
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging

load_dotenv()

ca = certifi.where()

uri = os.getenv("mongo_db_url")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=ca)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)