# In MongoDB, a collection is not created until it gets content
# You can check if a collection exist in a database by listing all collections:
# Example
# Return a list of all collections in your database:
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client['mydatabase']

mycol = db["customers"]

print(db.list_collection_names())

# Or you can check a specific collection by name:
# Example
# Check if the "customers" collection exists:
collist = db.list_collection_names()
if "customers" in collist:
  print("The collection exists.")
