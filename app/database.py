import os
from dotenv import load_dotenv # pip install python-dotenv

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


load_dotenv() #load environment variables
uri = os.environ.get("URI")

#Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["users_db"]
users_col = db["Users"]

def insert_user(username, name, email, password):
    return users_col.insert_one({"_id":username, "name":name, "email": email, "password": password})

def get_all_users():
    res = users_col.find()
    fnl = []
    for x in res:
        fnl.append(x)
    return fnl

def update_user(username, updates):
    """
    updates are in the form {key:newval}
    """
    myquery = {"_id": username}
    newval = {"$set":updates}

    users_col.update_one(myquery, newval)

# update_user("penny", {"name": "Pen Jamil"})

def delete_user(username):
    query = {"_id": username}
    users_col.delete_one(query)
