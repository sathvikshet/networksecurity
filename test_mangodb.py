import os
import pymongo
import certifi
from dotenv import load_dotenv

load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

client = pymongo.MongoClient(
    MONGO_DB_URL,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=5000
)

try:
    client.admin.command('ping')
    print("✅ Connected successfully!")
except Exception as e:
    print("❌ Error:", e)
