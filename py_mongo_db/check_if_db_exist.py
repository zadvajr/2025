#Check if database exists
# You can check if a database exist by listing all databases in you system:
# Example
# Return a list of your system's databases:
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

print(client.list_database_names())


# Or you can check a specific database by name:
dblist = client.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")

#you can loop through the list of databases
for x in dblist:
  print(x)
