# Sort the Result
# Use the sort() method to sort the result in ascending or descending order.
# The sort() method takes one parameter for "fieldname" and one parameter for "direction"
#     (ascending is the default direction).

# Example
# Sort the result alphabetically by name:
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
mycol = db['customers']

results = mycol.find()
sorted_results = results.sort('name')

for result in sorted_results:
    print(result)
