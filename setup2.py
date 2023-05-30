import mysql.connector
password=input("Enter password of your database:")
mydb=mysql.connector.connect(host="localhost",user='root',passwd=password,database="movie")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE theatre(v_mname CHAR(30),v_phno VARCHAR(10),v_tic VARCHAR(10),v_sex CHAR(1),v_fname CHAR(40),v_lname CHAR(40),v_passwd VARCHAR(9),v_userID VARCHAR(3) PRIMARY KEY,v_snacks CHAR(3))")
