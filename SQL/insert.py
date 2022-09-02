import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sirisha@2002",
    database="mydatabase"
)
mycursor = mydb.cursor()

sql = "insert into Customers(Name, DOB) values (%s, %s)"
val = ("Uma", "18-09-1970")
val1 = [
    ("Vamsi", "01-10-1994"),
    ("KrishnaChaithnaya", "16-06-1983")
]
mycursor.execute(sql, val)
mycursor.executemany(sql, val1)

mydb.commit()
print(mycursor.rowcount, "record inserted")
