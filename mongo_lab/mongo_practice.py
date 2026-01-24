from pymongo import MongoClient

# Simple connection string without username/password
connecturl = "mongodb://127.0.0.1:27017"

print("Connecting to mongodb server")
connection = MongoClient(connecturl)

db = connection.training
collection = db.mongodb_glossary

docs_to_insert = [
    {"database": "a database contains collections"},
    {"collection": "a collection stores the documents"},
    {"document": "a document contains the data in the form of key value pairs."}
]

print("Inserting documents into collection.")
collection.insert_many(docs_to_insert)

print("Printing the documents in the collection.")
for document in collection.find():
    print(document)

print("Closing the connection.")
connection.close()
