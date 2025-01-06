# Update Table
# You can update existing records in a table by using the "UPDATE" statement:
#Example: Overwrite the address column from "Valley 345" to "Canyon 123":
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sup@dm1n",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

# Important!: Notice the statement: mydb.commit(). It is required to make the changes, 
# otherwise no changes are made to the table.

# Notice the WHERE clause in the UPDATE syntax: The WHERE clause specifies which record or 
# records that should be updated. If you omit the WHERE clause, all records will be updated!