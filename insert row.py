import mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    usrt="root",
    password="",
    database="sasmithadb"
)
mycursor = mydb.cursor()
sql=="INSERT INTO customers(name,address,id)VALUES(%s,%s)"
val=("Ranl","money22")
mycursor.execute(sql,val)

mydb.commit()
print(mycursor.rowcount,"record inserted.")
