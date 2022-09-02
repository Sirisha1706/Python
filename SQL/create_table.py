import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sirisha@2002",
    database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("create table Customers(id auto_increment primary key, Name varchar(20), DOB varchar(10))")

