#Drop Only if exist
# If the table you want to delete is already deleted, or for any other reason does not exist - 
# you can use the IF EXISTS keyword to avoid getting an error.
# Example
# Delete the table "customers" if it exists:
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sup@dm1n",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)