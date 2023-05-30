import mysql.connector
password=input("Enter password of your database:")
mydb=mysql.connector.connect(host="localhost",user="root",passwd=password)
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE Movie")
mydb.close()




