# Movie-Reservation-System
 I contributed to a Python-based project, a Movie Reservation System, designed to streamline movie theater operations. Python's simplicity and versatility made it an ideal choice for developing the system. It's fulfilling to contribute to an efficient solution that empowers movie theaters with seamless reservation processes
import mysql.connector as sql
password=input("Enter password of your database:")
conn=sql.connect(host = 'localhost',user='root',passwd=password,database='movie')
c1=conn.cursor()
if conn.is_connected():
    print("Successfully Connected......")
else:
    print("Something went wrong............")


while True:
    print ("$$$$$$$$$$$$  movieEX BOOKING (AC & NON AC) $$$$$$$$$$$$$$")
    print ("1>>SIGN UP for newAC ticket")
    print ("2>>LOG IN to see AC ticket details")
    print("3>>SIGN UP fro new NON-AC ticket")
    print("4>>LOG IN to see NON-AC ticket details")
    print("5>>DEVELOPER OPTION for AC")
    print("6>>DEVELOPER OPTION for NON-AC")
    print("7>>TO EXIT")
    ch=int(input("Enter your choice :"))
    if ch==1:
        print("***************AC BOOKING********************")
        v_mname = input("Enter the movie name :")
        v_phno = input("Enter phone number :")
        v_tic = input("Enter total tickets :" )
        v_sex = input ("Enter your sex :" )
        v_fname = input ("Enter your first name :")
        v_lname = input ("Enter your last name :")
        v_passwd = input ("Enter your passwd :")
        v_userID = input ("Enter your userID :")
        v_snacks = input ("Want Snacks YES or NO :")
        v_ins="insert into theatre values( '{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(v_mname,v_phno,v_tic,v_sex,v_fname,v_lname,v_passwd,v_userID,v_snacks)
        c1.execute(v_ins)
        conn.commit()
        print (" ticket booked congrats")
        my_data=(v_userID,)
        q="SELECT * FROM theatre WHERE  v_userID=%s"
        c1.execute(q,my_data)
        record=c1.fetchall()
        for i in record:
            print(i)
        print ("Thank you for visiting pallavan theatre")
        print ("ratings")
        rating=int(input("Give rating to the cervices:"))
        print("*"*rating)
    if ch==2:
        v_userID=input("Enter UserID to see ticket details:")
        my_data=(v_userID,)
        q="SELECT * FROM theatre WHERE  v_userID=%s"
        c1.execute(q,my_data)
        record=c1.fetchall()
        for i in record:
            print(i)
    if ch==3:
        print("*******************NON AC BOOKING*******************")
        n_mname = input("Enter the monie name :")
        n_phno =int(input("Enter phone number :"))
        n_tic = input("Enter total tickets :" )
        n_sex = input ("Enter your sex :" )
        n_fname = input ("Enter your first name :")
        n_lname = input ("Enter your last name :")
        n_passwd = input ("Enter your passwd :")
        n_userID = input ("Enter your userID :")
        n_snacks = input ("Order your snacks :")
        query="insert into non_ac values( '{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(n_mname,n_phno,n_tic,n_sex,n_fname,n_lname,n_passwd,n_userID,n_snacks)
        c1.execute(query)
        conn.commit()
        print (" ticket booked congrats")
        rr_data=(n_userID,)
        s="SELECT * FROM non_ac WHERE  n_userID=%s"
        c1.execute(s,rr_data)
        record=c1.fetchall()
        for a in record:
            print(a)
        print ("Thank you for visiting pallavan theatre")
        print ("ratings")
        ratin=int(input("Give rating to the cervices:"))
        print("*"*ratin)
    if ch==4:
        n_userID=input("Enter UserID to see ticket details:")
        rr_data=(n_userID,)
        s="SELECT * FROM non_ac WHERE  n_userID=%s"
        c1.execute(s,rr_data)
        recordI=c1.fetchall()
        for b in recordI:
            print(b)
    if ch==5:
        z=int(input("ENTER PASSWORD:"))
        if z==4343:
            q1=("select * from theatre")
            c1.execute(q1)
            rec=c1.fetchall()
            for c in rec:
                print(c)
        else:
            print("..........WRONG PASSWORD..........")
            break
    if ch==6:
        m=int(input("ENTER PASSWORD:"))
        if m==5252:
            q2=("select * from non_ac")
            c1.execute(q2)
            reco=c1.fetchall()
            for x in reco:
                print(x)
        else:
            print("...................WRONG PASSWORD...............")
            break
    else:
        break
