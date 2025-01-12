# Advanced Query
# To make advanced queries you can use modifiers as values in the query object.
# E.g. to find the documents where the "address" field starts with the letter "S" 
# or higher (alphabetically), use the greater than modifier: {"$gt": "S"}:

# Example
# Find documents where the address starts with the letter "S" or higher:
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
customers_collection = db['customers']

myquery = { "address": {"$gt": "S"} }

results = customers_collection.find(myquery)

for result in results:
    print(result)