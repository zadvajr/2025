#To create a database mysql uses a CREATE DATABASE statement
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="sa",
    password="Sup@dm1n"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")