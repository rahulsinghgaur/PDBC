import mysql.connector as mc
con = mc.connect(host='localhost', user='root', password="", database="dbpython")

statement = con.cursor()
name = input("Enter Any Name: ")
query = f"update student set name='{name}' where id = 1001"

statement.execute(query)

con.commit()
