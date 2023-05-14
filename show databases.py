import mysql.connector
dbcon=mysql.connector.connect(host='localhost',user='root',password='')
db_cursor=dbcon.cursor()
db_cursor.execute("create database mydb1")
db_cursor.execute("show tables")
for db in db_cursor:
    print(db)
