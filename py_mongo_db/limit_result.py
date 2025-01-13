# Limit the Result
# To limit the result in MongoDB, we use the limit() method.

# The limit() method takes one parameter, a number defining how many documents to return.

# Consider you have a "customers" collection:

# Example
# Limit the result to only return 5 documents:
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
mycol = db['customers']

results = mycol.find().limit(5)

for result in results:
    print(result)
