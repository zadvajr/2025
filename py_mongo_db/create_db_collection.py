#Create DB Collection
# A collection in MongoDB is the same as a table in SQL databases.
# To create a collection in MongoDB, use database object and specify the name of the collection - 
# you want to create.
# MongoDB will create the collection if it does not exist.
# Example
# Create a collection called "customers":
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client['mydatabase']

mycol = db["customers"]

# collection created!
# Important: In MongoDB, a collection is not created until it gets content!
# MongoDB waits until you have inserted a document before it actually creates the collection.
# MongoDB waits until you have inserted a document before it actually creates the collection.