import pandas as pd
import pymysql
from os import system
import mysql.connector
import re
from sqlalchemy import create_engine
# make a regular expression
# for validating 

Id=[]
List_users=[]
Email_id=[]
phone_no=[]
Addresh=[]
Posts=[]
Salr=[]
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# for validating an Phone
Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
mydb = mysql.connector.connect(
    host="localhost",
   user="kundanagrawal",
   password="",
   database="employee_management")
connect = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}".format(user="kundanagrawal",
   pw="",
   db="employee_management"))
class heritage:

# Function to Add_Employee By kundan
 def menu(self):
    system("cls")
    print("{:>60}".format("************************************"))
    print("{:>60}".format("-->> Employee Management System <<--"))
    print("{:>60}".format("   ******************************By kundan Agrawal*******************"))
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Promote Employee Record")
    print("5. Remove Employee Record")
    print("6. Search Employee Record")
    print("7. Exit\n")
    print("{:>60}".format("-->> Choice Options: [1/2/3/4/5/6/7] <<--"))
    ch = int(input("Enter your Choice: "))
    if ch == 1:
        system("cls")
        user.add_employee()
    elif ch == 2:
        system("cls")
        user.display_employe()
    elif ch == 3:
        system("cls")
        user.update_employee()
    elif ch == 4:
        system("cls")
        user.Promote_Employ()
    elif ch == 5:
        system("cls")
        user.Remove_Employ()
    elif ch == 6:
        system("cls")
        user.Search_Employ()
    elif ch == 7:
        system("cls")
        print("{:>60}7".format("Have A NIce Day :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any key To Continue..")
        user.menu()
    user.menu()
 def __init__(self):
    import mysql.connector
    mydb = mysql.connector.connect(
    host="localhost",
   user="kundanagrawal",
   password="",
   database="employee_management")
 def check_employee_name(self,employee_name):
    sql = 'select * from empdata where Name=%s'
    # making cursor buffered to make
    # rowcount method work properly
    c = mydb.cursor(buffered=True)
    data = (employee_name,)

    # Execute the sql query
    c.execute(sql, data)

    # rowcount method to find number
    # of rowa with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False
# Function To Check if Employee With
# given Id Exist or not
 def check_employee(self,employee_id):
    # query to select all Rows from
    # employee(empdata) table
    sql = 'select * from empdata where Id=%s'

    # making cursor buffered to make
    # rowcount method work properly
    c = mydb.cursor(buffered=True)
    data = (employee_id,)

    # Execute the sql query
    c.execute(sql, data)

    # rowcount method to find number
    # of rowa with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False
 def add_employee(self):
    print("{:>60}".format("-->>Add Employee Record<<--"))
    Id=[]
    List_users=[]
    Email_id=[]
    phone_no=[]
    Addresh=[]
    Posts=[]
    Salr=[]
    Addres=[Addresh,Posts,Salr]
    records=int(input("Enter the number of Employee You want to add"))
    for i in range(records):
     Ids= input("Enter Employee Id: ")
      # checking If Employee Id is Exit Or Not
     if (user.check_employee(Ids) == True):
        print("Employee ID Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        user.add_employee()
     name=input("Enter the name of Employee")
     # checking If Employee Name is Exit Or Not
     if (user.check_employee_name(name) == True):
        print("Employee Name Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        user.add_employee()
     emails=str(input("Enter Employee Email ID: "))
     if(re.fullmatch(regex, emails)):
        print("Valid Email")
     else:
        print("Invalid Email")
        press = input("Press Any Key To Continue..")
        user.add_employee()
     Phone_nos = input("Enter Employee Phone No.: ")
     if(Pattern.match(Phone_nos)):
        print("Valid Phone Number")
     else:
         print("Invalid Phone Number")
         press = input("Press Any Key To Continue..")
         user.add_employee()
     Address = input("Enter Employee Address: ")
     Post = input("Enter Employee Post: ")
     Salary = input("Enter Employee Salary: ")
     List_users.append(name)
     Id.append(Ids)
     Email_id.append(emails)
     phone_no.append(Phone_nos)
     Addresh.append(Address)
     Posts.append(Post)
     Salr.append(Salary)
     # Instering Employee Details in
    # the Employee (empdata) Table

  
    
    # data=(20,["kundan"],"kundan@gmail.com",7061478272,"kumhar","software",20000000000000000)
    datas=pd.DataFrame({
        "Id":Id,
        "Name":List_users,
        "Emial_Id":Email_id,
        "Phone_no":phone_no,
        "Address":Addresh,
        "Post":Posts,
        "Salary":Salr
    })
    # print(datas)
    cols="`,`".join([str(i)for i in datas.columns.tolist()])
    for i,row in datas.iterrows():
        sql="INSERT INTO `empdata`(`"+cols+"`) VALUES("+"%s,"*(len(row)-1)+"%s)"
        c = mydb.cursor()
        c.execute(sql,tuple(row))
    sql = 'insert into empdata values(%s,%s,%s,%s,%s,%s,%s)'
   

    # Executing the sql Query

    # Commit() method to make changes in the table
#     import pymysql
#     from sqlalchemy import create_engine
#     connect = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}".format(user="kundanagrawal",
#    pw="",
#    db="employee_management"))
#     datas.to_sql('empdata',connect,if_exists='append',index=False)
    mydb.commit()
    print("Successfully Added Employee Record")
    press = input("Press Any Key")
    user.menu()
 def display_employe(self):
    print("{:>60}".format("-->> Display Employee Record <<--"))
    # query to select all rows from Employee (empdata) Table
    sql=pd.read_sql("select * from empdata",connect)
    print(sql)
    # sql = 'select * from empdata'
    # c = mydb.cursor()
 # Fetching all details of all the Employees
    # r = c.fetchall()
    # for i in r:
    #     print("Employee Id: ", i[0])
    #     print("Employee Name: ", i[1])
    #     print("Employee Email Id: ", i[2])
    #     print("Employee Phone No.: ", i[3])
    #     print("Employee Address: ", i[4])
    #     print("Employee Post: ", i[5])
    #     print("Employee Salary: ", i[6])
    #     print("\n")
    # Executing the sql query
    # c.execute(sql)
    press = input("Press Any key To Continue..")
    user.menu()
 def update_employee(self):
    print("{:>60}".format("-->> Update Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if(user.check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        user.menu(self)
    else:
        Emial_Id = input("Enter Employee Email ID: ")
        if(re.fullmatch(regex, Emial_Id)):
            print("Valid Email")
        else:
            print("Invalid Email")
            press = input("Press Any Key To Continue..")
            user.Update_Employ()
        Phone_no = input("Enter Employee Phone No.: ")
        if(Pattern.match(Phone_no)):
            print("Valid Phone Number")
        else:
            print("Invalid Phone Number")
            press = input("Press Any Key To Continue..")
            user.Update_Employ()
        Address = input("Enter Employee Address: ")
        # Updating Employee details in empdata Table
        sql = 'UPDATE empdata set Emial_Id = %s, Phone_no = %s, Address = %s where Id = %s'
        data = (Emial_Id, Phone_no, Address, Id)
        c = mydb.cursor()
        # Executing the sql query
        c.execute(sql, data)
        
        mydb.commit()
        print("Updated Employee Record")
        press = input("Press Any Key To Continue..")
        user.menu()
 def Promote_Employ(self):
    print("{:>60}".format("-->> Promote Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if(user.check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        user.menu()
    else:
        Amount  = int(input("Enter Increase Salary: "))
        #query to fetch salary of Employee with given data
        sql = 'select Salary from empdata where Id=%s'
        data = (Id,)
        c = mydb.cursor()
        
        #executing the sql query
        c.execute(sql, data)
        
        #fetching salary of Employee with given Id
        r = c.fetchone()
        t = r[0]+Amount
        #query to update salary of Employee with given id
        sql = 'update empdata set Salary = %s where Id = %s'
        d = (t, Id)

        #executing the sql query
        c.execute(sql, d)

        #commit() method to make changes in the table 
        mydb.commit()
        print("Employee Promoted")
        press = input("Press Any key To Continue..")
        user.menu()
 def Remove_Employ(self):
        print("{:>60}".format("-->> Remove Employee Record <<--\n"))
        Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
        if(user.check_employee(Id) == False):
          print("Employee Record Not exists\nTry Again")
          press = input("Press Any Key To Continue..")
          user.menu()
        else:
             sql = 'delete from empdata where Id = %s'
             data = (Id,)
             c = mydb.cursor()
             c.execute(sql,data)
             mydb.commit()
             print("Employee Removed")
        press = input("Press Any key To Continue..")
        user.menu()
                 
# Function to Search_Employ
 def Search_Employ(self):
     print("{:>60}".format("-->> Search Employee Record <<--\n"))
     Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
     if(user.check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        user.menu()
     else:
        #query to search Employee from empdata table
        sql = 'select * from empdata where Id = %s'
        data = (Id,)
        c = mydb.cursor()
        
        #executing the sql query
        c.execute(sql, data)

        #fetching all details of all the employee
        r = c.fetchall()
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Name: ", i[1])
            print("Employee Email Id: ", i[2])
            print("Employee Phone No.: ", i[3])
            print("Employee Address: ", i[4])
            print("Employee Post: ", i[5])
            print("Employee Salary: ", i[6])
            print("\n")
        press = input("Press Any key To Continue..")
        user.menu()
user=heritage()
print(user.menu())

