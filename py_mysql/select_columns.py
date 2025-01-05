#Select Columns
#To select only some of the columns in a table, use the SELECT statment followed by the column name(s)
#Exampl
#Select only the name and address column
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sup@dm1n",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for result in myresult:
    print(result)
