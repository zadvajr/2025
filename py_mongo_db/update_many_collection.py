# Update Many
# To update all documents that meets the criteria of the query, use the update_many() method.

# Example
# Update all documents where the address starts with the letter "S":
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
mycol = db['customers']

myquery = { 'address': {'$regex': '^S'}}
new_values = { '$set': {'address': 'Minnie'}}

updated = mycol.update_many(myquery, new_values)

print(updated.modified_count, " updated successfully!")
