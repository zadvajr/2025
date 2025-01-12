#Filter the Result
# When finding documents in a collection, you can filter the result by using a query object.
# The first argument of the find() method is a query object, and is used to limit the search.

# Example
# Find document(s) with the address "Park Lane 38":
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
customers_collection = db['customers']

results = customers_collection.find({'address': 'Park Lane 38'})

for result in results:
    print(result)
