import mysql.connector

#db details
mydb=mysql.connector.connect(user='root', passwd='root', host='localhost', database='test')

#using buffered option so that we can store multiple values and previous value isn't lost when taking new values.
mycursor=mydb.cursor(buffered=True) 

#basic menu
def Menu():
    print(">>>>><<<<<".center(140))
    print("MAIN MENU: Covid testing management".center(140))
    print(">>>>><<<<<".center(140))
    print("1. Create records".center(140))
    print("2. Display Records".center(140))
    print(" a. Sorted as per city".center(140))
    print(" b. Sorted as per district".center(140))
    print(" c. Sorted as per quantity available".center(140))
    print(" d. Back".center(140))
    print("4. Update Record".center(140))
    print("5. Delete Record".center(140))
    print("6. Exit".center(140))
    print("*"*140)

#sub menu
def MenuSort():
    print(" a. Sorted as per city".center(140)) 
    print(" b. Sorted as per district".center(140)) 
    print(" c. Sorted as per quantity available".center(140)) 
    print(" d. Back".center(140))

#function to create new table if it doesnt exist
def Create():
    try:
        mycursor.execute('create table testdb(CENTRENO varchar(10),CENTRENAME varchar(20),MOBILE varchar(10),EMAIL varchar(20),ADDRESS varchar(20),CITY varchar(10),DISTRICT varchar(20),KITSAVAIL integer(15))')
        print("Table Created")
        Insert()

    except:
        print("Table Exist")
        Insert()

#function to insert new values
def Insert():
    while True:
        Acc=input("Enter account no") CENTRENAME=input("Enter CENTRENAME") Mob=input("Enter Mobile") email=input("Enter Email") Add=input("Enter Address") City=input("Enter City") DISTRICT=input("Enter DISTRICT") Bal=float(input("Enter kitsavail
        "))
        Rec=[Acc,CENTRENAME.upper(),Mob,email.upper(),Add.upper(),City.upper(),Country.upper(),Bal]
        Cmd="insert into testdb values(%s,%s,%s,%s,%s,%s,%s,%s)" mycursor.execute(Cmd,Rec)
        mydb.commit()
        ch=input("Do you want to enter more records")
        if ch=='N' or ch=='n':
            break

#function to display  by centre number    
def DispSortAcc():
    try:
        cmd="select * from testdb order by CENTRENO" 
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("CENTRENO","CENTRENAME","MOBILE","EMAIL ADDRESS","COMPLETE ADDRESS","CITY","DISTRICT","BALANCE"))
        print("="*125)
        for i in S:
            for j in i:
                print("%14s" % j, end=' ')
            print()
            print("="*125)
    except:
        print("Table doesn't exist")

#function to display  by centre name
def DispSortCENTRENAME():
    try:
        cmd="select * from testdb order by CENTRENAME"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("CENTRENO","CENTRENAME","MOBILE","EMAIL ADDRESS","COMPLETE ADDRESS","CITY","DISTRICT","BALANCE"))
        print("="*125)
        for i in S:
            for j in i:
                print("%14s" % j, end=' ')
            print()
        print("="*125)
    except:
        print("Table doesn't exist")

#function to display  by test kit balance
def DispSortBal():
    try:
        cmd="select * from testdb order by BALANCE" mycursor.execute(cmd)
        S=mycursor.fetchall()
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("CENTRENO","CENTRENAME","MOBILE","EMAIL ADDRESS","COMPLETE ADDRESS","CITY","DISTRICT","BALANCE")) print("="*125)
        for i in S:
            for j in i:
                print("%14s" % j, end=' ')
            print()
        print("="*125)
    except:
        print("Table doesn't exist")

#function to search by account number
def DispSearchAcc(): 
    try:
        cmd="select * from testdb"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        ch=input("Enter the accountno to be searched")
        for i in S:
            if i[0]==ch:
                print("="*125)
                F="%15s %15s %15s %15s %15s %15s %15s %15s"
                print(F % ("CENTRENO","CENTRENAME","MOBILE","EMAIL ADDRESS","COMPLETE ADDRESS","CITY","DISTRICT","BALANCE"))
                print("="*125)
                for j in i:
                    print('%14s' % j,end=' ')
                print()
                break
            else:
                print("Record Not found")
    except:
        print("Table doesn't exist")

#function to update values
def Update():
    try:
        cmd="select * from testdb"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        A=input("Enter the accound no whose details to be changed")
        for i in S:
            i=list(i)
            if i[0]==A:
                ch=input("Change CENTRENAME(Y/N)")
                if ch=='y' or ch=='Y':
                    i[1]=input("Enter CENTRENAME")
                    i[1]=i[1].upper()

                ch=input("Change Mobile(Y/N)")
                if ch=='y' or ch=='Y':
                    i[2]=input("Enter Mobile")

                ch=input("Change Email(Y/N)")
                if ch=='y' or ch=='Y':
                    i[3]=input("Enter email")
                    i[3]=i[3].upper()

                ch=input("Change Address(Y/N)")
                if ch=='y' or ch=='Y':
                    i[4]=input("Enter Address")
                    i[4]=i[4].upper()

                ch=input("Change city(Y/N)")
                if ch=='y' or ch=='Y':
                    i[5]=input("Enter City")
                    i[5]=i[5].upper()

                ch=input("Change DISTRICT(Y/N)")
                if ch=='y' or ch=='Y':
                    i[6]=input("Enter DISTRICT")
                    i[6]=i[6].upper()

                ch=input("Change kitsavail
                (Y/N)")
                if ch=='y' or ch=='Y':
                    i[7]=float(input("Enter kitsavail
                    "))
                cmd="UPDATE testdb SET CENTRENAME=%s,MOBILE=%s,EMAIL=%s,ADDRESS=%s,CITY=%s,DISTRICT=%s,BALANCE=%s WHERE CENTRENO=%s"
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0]) mycursor.execute(cmd,val)
                mydb.commit()
                print("Account Updated")
                break
            else:
                print("Record not found")
    except:
        print("No such table")

#function to delete values
def Delete():
    try:
        cmd="select * from testdb"
        mycursor.execute(cmd)
        S=mycursor.fetchall()
        A=input("Enter the centre no whose details to be changed")
        for i in S:
            i=list(i)
            if i[0]==A:
                cmd="delete from testdb where CENTRENO=%s" val=(i[0],) mycursor.execute(cmd,val) mydb.commit()
                print("Account Deleted")
                break
            else:
                print("Record not found")
    except:
        print("No such Table")

#main loop w/ choices
while True:
    Menu()
    ch=input("Enter your Choice")
    if ch=="1":
        Create()
    elif ch=="2":
        while True:
            MenuSort()
            ch1=input("Enter choice a/b/c/d")
            if ch1 in ['a','A']:
                DispSortAcc()
            elif ch1 in ['b','B']:
                DispSortCENTRENAME()
            elif ch1 in ['c','C']:
                DispSortBal()
            elif ch1 in ['d','D']:
                print("Back to the main menu")
                break
            else:
                print("Invalid choice")
    elif ch=="3":
        DispSearchAcc()
    elif ch=="4":
        Update()
    elif ch=="5":
        Delete() 
    elif ch=="6":
        while True:
    elif ch=="7":
        print("Exiting...")
        break
    else:
        print("Wrong Choice Entered")

#end of program