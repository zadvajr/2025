import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sup@dm1n"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASE")

for db in mycursor:
    print(db)