# Update Collection
# You can update a record, or document as it is called in MongoDB, by using the update_one() method.
# The first parameter of the update_one() method is a query object defining which document to update.

# Note: If the query finds more than one record, only the first occurrence is updated.

# The second parameter is an object defining the new values of the document.

# Example
# Change the address from "Valley 345" to "Canyon 123":
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
mycol = db['customers']

myquery = { "address": "Valley 345" }
newvalue = { "$set": {'address': 'Canyon 123'}}

mycol.update_one(myquery, newvalue)

#Print customers after the update
for customer in mycol.find():
    print(customer)
