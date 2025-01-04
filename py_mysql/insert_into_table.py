#To fill a table in MySQL, use the "INSERT INTO" statement.
# Example
# Insert a record in the "customers" table:
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sup@dm1n",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record added successfully!")

#Notice the statement: mydb.commit(). 
# It is required to make the changes, otherwise no changes are made to the table.