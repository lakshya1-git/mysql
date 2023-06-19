import mysql.connector as connection

mydb = connection.connect(host="localhost", user="root", password="mysql123")
cursor = mydb.cursor()
cursor.execute("inssert into lakshya.lakshyadetails values(101,'name1', 'ipdata','laksh@gmail',2)")
print(mydb)
mydb.commit()
