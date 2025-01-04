#Get Inserted ID
#YOu can get the id of the row you just inserted by asking the cursor object
#If you insert more than one row, the id of the last inserted row is returned.
#Example: Insert one row and return the ID
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sup@dm1n",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)