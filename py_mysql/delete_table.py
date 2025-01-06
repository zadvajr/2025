#Delete Table
# You can delete an existing table by using the "DROP TABLE" statement:
#Example: Delete the table "customers":
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sup@dm1n",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)