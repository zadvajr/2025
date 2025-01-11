# A document in MongoDB is the same as a record in SQL databases.
# To insert a record, or document as it is called in MongoDB, into a collection, we use the insert_one() method.
# The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s) -
# of each field in the document you want to insert.
# Example
# Insert a record in the "customers" collection:
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
mycol = db["customers"]

mydict = { "_id": 31, "name": "Mary", "address": "Abeokuta 9" }

inserted_data = mycol.insert_one(mydict)

print(inserted_data)
print(inserted_data.inserted_id)
