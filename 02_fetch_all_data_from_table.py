import mysql.connector as mc
con = mc.connect(host='localhost', user='root', password="", database="dbpython")

statement = con.cursor()

query = "select * from student;"

statement.execute(query)

result = statement.fetchall()
for data in result:
    print(data)
