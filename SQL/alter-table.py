import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sirisha@2002",
    database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("alter table Customers add column id int auto_increment primary key")
mycursor.execute("show tables")
for x in mycursor:
    print(x)

