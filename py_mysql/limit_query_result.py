#Limit the result
#You can limit the number of records return from a query by using the LIMIT statement
#For example: Select 5 first records from the customers table
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sup@dm1n",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for result in myresult:
    print(result)

