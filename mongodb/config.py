from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

# URL-encode the password
username = "zadva"
password = "2614@Vara"
encoded_password = quote_plus(password)

# Construct the correct URI
uri = f"mongodb+srv://{username}:{encoded_password}@cluster0.dq8vj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
