# Delete Many Documents
# To delete more than one document, use the delete_many() method.
# The first parameter of the delete_many() method is a query object defining which documents to delete.

# Example
# Delete all documents were the address starts with the letter S:
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
mycol = db['customers']

myquery = { "address": {"$regex": "^S"}}

deleted = mycol.delete_many(myquery)

print(deleted.deleted_count, " deleted successfully!")
