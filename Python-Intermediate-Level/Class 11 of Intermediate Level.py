import firebase_admin
from firebase_admin import credentials
#Firebase Realtime Database
cred = credentials.Certificate("Class 11.json")
firebase_admin.initialize_app(cred)
