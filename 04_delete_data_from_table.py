import mysql.connector as mc
con= mc.connect(host='localhost', user='root', password="", database="dbpython")

statement = con.cursor()

query = "delete from student where id = 103"

statement.execute(query)

con.commit()