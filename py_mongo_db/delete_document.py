# Delete Document
# To delete one document, we use the delete_one() method.
# The first parameter of the delete_one() method is a query object defining which document to delete.
# Note: If the query finds more than one document, only the first occurrence is deleted.

# Example
# Delete the document with the address "Jones Str. 9":
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
mycol = db['customers']

myquery = {"address": "Jones Str. 9"}

deleted_customer = mycol.delete_one(myquery)

print(deleted_customer, " deleted successfully!")
