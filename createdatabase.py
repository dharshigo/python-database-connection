import mysql.connector
dbcon=mysql.connector.connect(host='localhost',user='root',password='')
db_cursor=dbcon.cursor()
db_cursor.execute("create database pythondb2")
db_cursor.execute("SHOW DATABASES")
for db in db_cursor: # print database names
    print(db)


