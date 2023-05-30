import mysql.connector
password=input("Enter password of your database:")
mydb=mysql.connector.connect(host="localhost",user='root',passwd=password,database="movie")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE non_ac(n_mname CHAR(30),n_phno VARCHAR(10),n_tic VARCHAR(10),n_sex CHAR(1),n_fname CHAR(40),n_lname CHAR(40),n_passwd VARCHAR(9),n_userID VARCHAR(3) PRIMARY KEY,n_snacks CHAR(3))")

