import mysql.connector

# create database 

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE street")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)

