# Insert Documents
There are 2 methods to insert documents into a MongoDB database.

# insertOne()
To insert a single document, use the insertOne() method.

This method inserts a single object into the database.

Note: When typing in the shell, after opening an object with curly braces "{" you can press enter to start a new line in the editor without executing the command. The command will execute when you press enter after closing the braces.

# Example
db.posts.insertOne({
  title: "Post Title 1",
  body: "Body of post.",
  category: "News",
  likes: 1,
  tags: ["news", "events"],
  date: Date()
})