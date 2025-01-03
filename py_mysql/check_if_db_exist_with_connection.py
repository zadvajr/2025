import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sup@dm1n",
    database="mydatabase"
)

#If you run this file without an error it means database "mydatabase" exists.