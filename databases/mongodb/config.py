
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()
MONGODB_URL = os.getenv('MONGODB_URI')

client = MongoClient(MONGODB_URL, server_api=ServerApi('1'))

db = client.todo_db
collection = db["todo_data"]
