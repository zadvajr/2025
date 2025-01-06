#ORDER BY Statement
#Sort the result
#Use the ORDER BY  statement to sort the result either in ascending or descending order
#The ORDER BY keyword sorts the result in ascending order by default.
#If you you want the result in descending order, use DESC keyword
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sup@dm1n",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for result in myresult:
    print(result)