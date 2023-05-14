import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="sasmithadb")
mycursor=mydb.cursor()
sql="INSERT INTO customers(name,address)VALUES(%s,%s)"
val=[('GOTA','singapore'),('MAHINDA','hambanthota')]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"wasinsetrted")
