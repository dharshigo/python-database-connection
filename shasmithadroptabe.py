import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="sasmithadb")
mycursor=mydb.cursor()
mycursor.execute("drop table customers")
mydb.commit()
