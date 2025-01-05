#Using fetchone() method
#If you are interested in one row, you can use fetchone() method
#The fetchone() method will return the first row of the result.
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sup@dm1n",
    database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)