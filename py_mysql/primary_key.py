#when creating a table, you should also create a table with unique key for each record
#This can be done by defining a PRIMARY KEY
#We use the statement "INT AUTO_INCREMENT PRIMARY KEY" 
# which will insert a unique number for each record. Starting at 1, and increased by one for each record.
#Example
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY,\
#  name VARCHAR(255), address VARCHAR(255))")


#Since we've created the table already in the previous exercise
#We will use ALTER TABEL and ADD COLUMN Statments to update the previous table.
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sup@dm1n",
    database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
