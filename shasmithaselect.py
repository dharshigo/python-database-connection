import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="sasmithadb")
mycursor=mydb.cursor()
mycursor.execute("select*from customers where name='GOTA'")
result=mycursor.fetchall()
for i in result:
    print(i) 
