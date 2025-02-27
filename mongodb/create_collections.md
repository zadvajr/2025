# Create Collection using mongosh
There are 2 ways to create a collection.

## Method 1
You can create a collection using the createCollection() database method.

### Example
db.createCollection("posts")

## Method 2
You can also create a collection during the insert process.

### Example
We are here assuming object is a valid JavaScript object containing post data:

db.posts.insertOne(Object)