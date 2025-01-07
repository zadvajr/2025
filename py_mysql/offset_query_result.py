#Start from another position
#If you want to return 5 records starting from the 3rd record you can use OFFSET statement
#Example: Start from position 3 and return 5 records
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sup@dm1n",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for result in myresult:
    print(result)