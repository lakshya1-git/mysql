import mysql.connector as conn

mydb = mysql.connector.connect(host="localhost", user="root", password="mysql123")
cursor = mydb.cursor()
z = "insert into test values(101, 'lakshya', 'pandey@961gmail.com', 100, 34)"
cursor.execute(z)
mydb.commit()
print(mydb)
cursor. execute("select * from test")
for i in cursor.fetchall():
    print(i)