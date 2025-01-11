# In MongoDB we use the find() and find_one() methods to find data in a collection.
# Just like the SELECT statement is used to find data in a table in a MySQL database.

# Find One
# To select data from a collection in MongoDB, we can use the find_one() method.
# The find_one() method returns the first occurrence in the selection.

# Example
# Find the first document in the customers collection:
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["mydatabase"]

customer_collection = db["customers"]

result = customer_collection.find_one({'name': 'Zadva'})

print(result)
