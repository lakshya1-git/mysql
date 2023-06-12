import mysql.connector as connection

mydb = connection.connect(host="localhost", user="root", password="mysql123")
print(mydb)

cursor = mydb.cursor()

cursor.execute("create database lakshya")  # create database
cursor.execute("show databases")

for database in cursor:
    print(database)

cursor.execute("use lakshya")
cursor.execute(
    "create table laksdetails(employee_id int(10), employee_name varchar(80), employee_mail varchar(20), employee_sal int(6),employee_att int(2))")

cursor.execute("select * from laksdetails")
print(cursor.fetchall())

cursor.close()
mydb.close()