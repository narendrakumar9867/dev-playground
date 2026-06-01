import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials, firestore
from os import getenv

load_dotenv()

# Initialize Firebase Admin using service account credentials
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()

