# Exclude a field
# Example
# This example will exclude "address" from the result:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find({},{ "address": 0 }):
  print(x)


# Example
# You get an error if you specify both 0 and 1 values in the same object 
# (except if one of the fields is the _id field):
# This section will produce an error
# for x in mycol.find({},{ "name": 1, "address": 0 }):
#   print(x)