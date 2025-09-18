import os
import sys
import pandas as pd
import pymongo
import certifi
from dotenv import load_dotenv
from pymongo.errors import ConnectionFailure, BulkWriteError

# Load .env file
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
ca = certifi.where()


class NetworkDataExtract:
    def cv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = data.to_dict(orient="records")
            print(f"Loaded {len(records)} records from CSV.")
            return records
        except FileNotFoundError:
            print(f"Error: File not found -> {file_path}")
            return []
        except Exception as e:
            print(f"Error reading CSV: {e}")
            return []

    def insert_data_to_mongo(self, records, database, collection):
        if not records:
            print("No records to insert.")
            return 0
        try:
            client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca, serverSelectionTimeoutMS=5000)
            # Ping server to ensure connection
            client.admin.command('ping')
            db = client[database]
            coll = db[collection]
            try:
                coll.insert_many(records, ordered=False)  # ordered=False continues on duplicates
                print(f"Inserted {len(records)} records successfully")
                return len(records)
            except BulkWriteError as bwe:
                print(f"Bulk write error: {bwe.details}")
                return len(records) - len(bwe.details.get('writeErrors', []))
        except ConnectionFailure as cf:
            print(f"Connection to MongoDB failed: {cf}")
            return 0
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0


if __name__ == "__main__":
    FILE_PATH = r"Network_Data\phisingData.csv"
    DATABASE = "SATHVIK"
    COLLECTION = "NETWORK_SECURITY"

    networkobj = NetworkDataExtract()
    records = networkobj.cv_to_json_convertor(FILE_PATH)
    print(records[:5])  # Preview first 5 records
    no_of_records = networkobj.insert_data_to_mongo(records, DATABASE, COLLECTION)
    print(f"Total number of records inserted: {no_of_records}")
