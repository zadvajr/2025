# Return the _id Field
# The insert_one() method returns a InsertOneResult object, which has a property, inserted_id
# that holds the id of the inserted document.
# Example
# Insert another record in the "customers" collection, and return the value of the _id field:
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
mycol = db['customers']

mydict = { "name": "Peter", "address": "Lowstreet 27" }

x = mycol.insert_one(mydict)

print(x.inserted_id)

# If you do not specify an _id field, then MongoDB will add one for you and assign a unique id for each document.
# In the example above no _id field was specified, so MongoDB assigned a unique _id for the record (document).