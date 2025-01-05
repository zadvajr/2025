#MySQL Where Statement
#Selecting with a filter
#When selecting records from a table, you can filter the selection by using WHERE statement
#Example:
# Select record(s) where the address is "Park Lane 38": result:
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sup@dm1n",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers WHERE address='Park Lane 38'")

myresult = mycursor.fetchall()

for result in myresult:
    print(result)
