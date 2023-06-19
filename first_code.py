import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="mysql123")
print(mydb)

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE test")  # Create database
cursor.execute("SHOW DATABASES")
for database in cursor:
    print(database)

cursor.execute("USE test")
cursor.execute("CREATE TABLE testdetails(employee_id INT(10), employee_name VARCHAR(80), employee_mail VARCHAR(20), employee_sal INT(6), employee_att INT(2))")
cursor.execute("SELECT * FROM testdetails")
print(cursor.fetchall())

cursor.close()
mydb.close()
