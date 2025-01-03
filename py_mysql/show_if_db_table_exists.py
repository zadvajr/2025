#Show if db table exists
#You can check if a table exist by listing all tables in your database with the "SHOW TABLES" statement:
#Return a list of your system's databases:
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sup@dm1n",
    database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for table in mycursor:
    print(table)