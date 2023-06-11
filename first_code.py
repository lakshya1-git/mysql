import mysql.connector as connection
mydb = connection.connect(host= "localhost", user = "root", password="mysql123")
print(mydb)
cursor = mydb.cursor()
cursor.execute("create databaase lakshya") #create data base
cursor.execute("show database")
cursor.execute("create database")
cursor.execute("create table lakshya.laksdetails()")
print(cursor.fetchall())