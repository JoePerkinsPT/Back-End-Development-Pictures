from pymongo import MongoClient

# Simple connection string without username/password
connecturl = "mongodb://127.0.0.1:27017"

print("Connecting to mongodb server")
connection = MongoClient(connecturl)

db = connection.training
collection = db.python

doc = {"lab": "Accessing mongodb using python", "Subject": "No SQL Databases"}
print("Inserting a document into collection.")
collection.insert_one(doc)

docs = collection.find()
print("Printing the documents in the collection.")
for document in docs:
    print(document)

print("Closing the connection.")
connection.close()
