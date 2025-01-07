"""Join two tables using INNER JOIN"""
#Join Two or More Tables
# You can combine rows from two or more tables, based on a related column between them,  -
# by using a JOIN statement.
# Consider you have a "users" table and a "products" table:
# These two tables can be combined by using users' fav field and products' id field.
# Example
# Join users and products to see the name of the users favorite product:
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sup@dm1n",
    database="mydatabase"
)

mycursor = mydb.cursor()

SQL = ''' SELECT users.name AS users, \
    products.name AS favorites \
    FROM users \
    INNER JOIN products ON users.fav = products.id
    '''
mycursor.execute(SQL)

myresult = mycursor.fetchall()

for result in myresult:
    print(result)

# Note: You can use JOIN instead of INNER JOIN. They will both give you the same result.
