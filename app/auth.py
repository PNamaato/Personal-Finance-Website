# Handles user authentication (login/logout)
import streamlit as st
import streamlit_authenticator as stauth # pip install streamlit-authenticator

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://peninahpaula:bpkZSKxYCBPWcrD3@cluster0.mf8td.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


