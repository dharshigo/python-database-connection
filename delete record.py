import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="sasmithadb")
mycursor=mydb.cursor()
mycursor.execute("delete from customers where name='GOTA'")
mydb.commit()
print(mycursor.rowcount,"record(s)deleted")
