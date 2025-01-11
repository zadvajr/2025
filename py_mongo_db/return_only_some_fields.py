# Return Only Some Fields
# The second parameter of the find() method is an object describing which fields to include in the result.
# This parameter is optional, and if omitted, all fields will be included in the result.
# Example
# Return only the names and addresses, not the _ids:
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
mycol = db["customers"]

results = mycol.find({}, { "_id": 0, "name": 1, "address": 1 })
for result in results:
  print(result)

# You are not allowed to specify both 0 and 1 values in the same object 
# (except if one of the fields is the _id field). If you specify a field with the value 0,
# all other fields get the value 1, and vice versa: