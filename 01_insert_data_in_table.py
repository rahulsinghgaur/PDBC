import mysql.connector
con = mysql.connector.connect(
    host='localhost', user='root', password="", database="dbpython")

statement = con.cursor()

s = "insert into student values(%s, %s ,%s);"
s1 = (1010, 'shivam', "09881641")
statement.execute(s, s1) 
# execute(s)  ->s = "insert into student values(1001, 'gaur' ,'5678');"
# executemany(s,listName) -> listName = [(1001, 'gaur' ,'5678'),(1007, 'guru' ,'5667'), ......]
# executemany function is use to insert many records in database ok
con.commit()
