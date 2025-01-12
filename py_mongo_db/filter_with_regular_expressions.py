# Filter With Regular Expressions
# You can also use regular expressions as a modifier.
# Regular expressions can only be used to query strings.
# To find only the documents where the "address" field starts with the letter "S", 
# use the regular expression {"$regex": "^S"}:

# Example
# Find documents where the address starts with the letter "S":
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
customers_collection = db['customers']

myquery = { 'address': {'$regex': '^S'}}

results = customers_collection.find(myquery)

for result in results:
    print(result)
