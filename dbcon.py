import mysql.connector
dbcon=mysql.connector.connect(host='localhost',user='root',password='')
print(dbcon)
