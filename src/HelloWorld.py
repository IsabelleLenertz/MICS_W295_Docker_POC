import os
from time import sleep
from pymongo import MongoClient

sleep(2)
print("Hello World")

students = [
                {"name":"Mike"}, 
                {"name": "Daniel"},
                {"name": "George"}, 
                {"name": "Sophia"}, 
                {"name": "Edward"}, 
                {"name":"Unknown"}
            ]
db_endpoint = os.getenv('DB_URL')
print("connecting to db")

mongo_client = MongoClient(db_endpoint)
db_name = "W295"
collection_name = "students"
db = mongo_client[db_name]
collection = db[collection_name]
print("connected to db")

#Inserting a student
for s in students:
    if collection.count_documents(s) == 0:
        print("inserting ", s['name'])
        collection.insert_one(s)
        break
    
#Print collection
cursor = collection.find({})
for document in cursor:
    print(document)
    
        