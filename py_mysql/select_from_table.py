#Select from a table
#TO select from a table in MySQL you use the SELECT statement.
#Example
#Select all from the customers table and display the result.
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sup@dm1n",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for result in myresult:
    print(result)


#We use the fetchall() method, which fetches all rows from the last executed statement.