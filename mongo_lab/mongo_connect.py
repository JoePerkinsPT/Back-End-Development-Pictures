from pymongo import MongoClient

# Simple connection string without username/password
connecturl = "mongodb://127.0.0.1:27017"

print("Connecting to mongodb server")
connection = MongoClient(connecturl)

print("Getting list of databases")
dbs = connection.list_database_names()

for db in dbs:
    print(db)

print("Closing the connection to the mongodb server")
connection.close()
