import re,datetime
from setting import mysql_connection


## write a function to check if a number has string or  not
def has_numbers(inputString):
    if any(x.isdigit() for x in inputString):
        return False 
    if len(inputString)<5:
        return False
    return {'Valid':True, 'name':inputString}
    
def has_number(inputString):   
      
    if len(inputString)<8:
            return False
           
    if not any(x.isdigit() for x in inputString):
            return False
           
    return {'valid':True , 'password':inputString}
 
##
# write a function for for validating an Email
def check_email(email):
    regex=re.compile(r"([A-Za-z0-9]+[.\-_])*[A-Za-z0-9]+@[A-Za-z0-9\-]+(\.[A-Za-z]{2,})")
    # pass the regular expression
    if re.fullmatch(regex,email):
    # and the string into the fullmatch() method
        return {'valid':True,'email':email}
    else:
    #return Boolean Value
        #print("Enter Valid email")
        return False

def usernamevalidation(inputString):
    if len(inputString)<6:
        return False
    return {'valid':True,'username':inputString}
## form to validate
def register(registration_form): 
    
    #your input from your input string (assume from front end , json)
     
    #name lenth should be greater than 3 and should not have any digits
    if not has_numbers(registration_form['name']):
        return ({'valid':False,"message":"the name should have a minimum length of 4 characters and must not contain any digits."}) #(input("Enter Name : "))
    ## check email validation here 
    if not check_email(registration_form['email']):
       return ({'valid':False,"message":"Invalid email."})
    ## password should be greater than 8 digits and must have numbers, reuse has_number function
    if not has_number(registration_form['password']):
        return ({'valid':False,"message":"password should be greater than 8 digits and must have numbers."})
    
    if not usernamevalidation(registration_form['username']):
        return ({'valid':False,"message":"the username must have a minimum length of 5 characters."})#input("Enter UserName : ")
    
    registration_form['dob']#input("enter you DOB in formate(dd/mm/yyyy) : ")
    registration_form['valid']=True
    return registration_form
    
def capture_data(registration_form):
    
    ## if registration is valid
    data = register(registration_form)
    if data['valid']:
        
       
        ## connect with database
        mydb = mysql_connection()
        ## returns cursor
        
        
        ## check if username already in database, use 'where' clause
        ## if 
        print(data['username'])
        if checkExistUserName(data['username'],mydb):
            return ("username already taken, try another username.")
        else:
            inserRecord(data,mydb)
            print("Record inserted successfully")
        #if username not taken create a new record, insert values into table
        mydb.close()
        return data
    else:
        return data['message']
        
def inserRecord(data,conn):
    
    name=data['name']
    user_name=data['username']
    date_value=data['dob']
    password_value=data['password']
    email_value=data['email']
    
    insertsql=conn.cursor()
    
    query=f"insert into my_users (name,username,email,date,password) values(%s,%s,%s,%s,%s)"
    val=(name,user_name,email_value,date_value,password_value)
    insertsql.execute(query,val)
    conn.commit()
    insertsql.close()
    
#check exist username 
def checkExistUserName(username,conn):
    sql=conn.cursor()
    query=f"select count(*) from my_users where username=%s"
    sql.execute(query,(username,))
    res=sql.fetchone()
    return res[0]>0
    

#do not delete following function
def task_runner():
    ## Test data
    name ='test username'
    user_name = 'testusername'
    email_value = 'test@testgmail.com'
    date_value = '15-12-1999'
    password_value = 'testdfs77ds'
    registration_form = {'name' : name,  'username' :user_name, 'email': email_value, 'dob' : date_value, 'password': password_value}
    print(capture_data(registration_form))
    #print(registration_form)

task_runner()