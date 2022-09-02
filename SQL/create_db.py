import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sirisha@2002"
)
mycursor = mydb.cursor()
mycursor.execute("create database mydatabase")
