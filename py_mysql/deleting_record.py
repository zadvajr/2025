#Delete Record
#You can delete records from an existing table by using the DELETE FROM  statement
# Example
# Delete any record where the address is "Mountain 21":
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sup@dm1n",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address='Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted!")

# Important!: Notice the statement: mydb.commit().
# It is required to make the changes, otherwise no changes are made to the table.

# Notice the WHERE clause in the DELETE syntax: The WHERE clause specifies which record(s) that should be deleted.
# If you omit the WHERE clause, all records will be deleted!