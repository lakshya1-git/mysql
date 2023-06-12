import mysql.connector as connection
mydb = connection.connect(host= "localhost", user = "root", password="mysql123")
print(mydb)
cursor = mydb.cursor()
cursor.execute("create databaase lakshya") #create data base
cursor.execute("show database")
cursor.execute("create database")
cursor.execute("create table lakshya.laksdetails(employee_id in(10), employee_name varchar(80), employee_mail varchar(20), employee_sal int(6),employee_att int(2))")
cursor.execute(s)
print(cursor.fetchall())