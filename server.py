from typing import Counter
import mysql.connector
from bottle import route, run, template
from bottle import get, post
from bottle import request, redirect
import smtplib
import string
import random

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "dataproject"
    )


## access code generator

def access_code_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def k_anonymity(counter, age):
    general_age = str(age)
    if counter < 3:
            if age < 10:
                general_age = '>0'

            if age > 10 and age < 20:
                general_age = '>10'

            if age > 20 and age < 30:
                general_age = '>20'

            if age > 30 and age < 40:
                general_age = '>30'

            if age > 40 and age < 50:
                general_age = '>40'
            
            if age > 50 and age < 60:
                general_age = '>50'

            if age > 60 and age < 70:
                general_age = '>60'
            
            if age >= 80:
                general_age = '>70'
        
    else:
        general_age = general_age[:-1]
        general_age = general_age + '*'
       # print("Past 3 = " + general_age)


    return general_age


#mycursor = db.cursor()

#mycursor.execute( 'SELECT * FROM accounts')
#mycursor.execute("INSERT INTO accounts (username, password) VALUES(%s,%s)", (name,password))
#db.commit
#print(data)

#data = []
#for x in mycursor:
 #   data.append(x)
    #print(x)

#print(data[0])

#string = data[0]
#print(string)

mycursor = db.cursor(buffered=True)

@route("/")
def get_index():
    return template("index")

@route("/useraccount")
def get_useraccount():
    return template("useraccount")

## routes to the admin page and can admin can view requests
@route("/adminpage")
def get_adminpage():

    mycursor.execute('SELECT fullname FROM request')
    request_names = []
    ## cleaning up string in table
    for x in mycursor:
        name = ""
        for j in str(x):
            if j !='(' and j !=')' and j !=',':
                name = name + j
        request_names.append(name)

    #print(data)
    emails = []
    mycursor.execute('SELECT email FROM request')
    for x in mycursor:
        email = ""
        for j in str(x):
            if j !='(' and j !=')' and j !=',':
                email = email + j
        emails.append(email)

    return template("adminpage", names = request_names, emails = emails)

# routes to user account and 
@route("/useraccount")
def get_useraccount():
    names = []
    ages = []
    symthom1s = []
    symthom2s = []
    mycursor.execute('SELECT name FROM publiccovidinfo')

    ## cleaning up strings for names list
    for x in mycursor:
        name = ""
        for j in str(x):
            if j !='(' and j !=')' and j !=',':
                name = name + j
        names.append(name)
 
    mycursor.execute('SELECT age FROM publiccovidinfo')
    for x in mycursor:
        age = ""
        for j in str(x):
            if j !='(' and j !=')' and j !=',':
                age = age + j
        ages.append(age)

    mycursor.execute('SELECT symthom1 FROM publiccovidinfo')
    for x in mycursor:
        symthom = ""
        for j in str(x):
            if j !='(' and j !=')' and j !=',':
                symthom = symthom + j
        symthom1s.append(symthom)

    mycursor.execute('SELECT symthom2 FROM publiccovidinfo')
    for x in mycursor:
        symthom = ""
        for j in str(x):
            if j !='(' and j !=')' and j !=',':
                symthom = symthom + j
        symthom2s.append(symthom)

    return template("useraccount", names = names, ages = ages, symthom1s = symthom1s, symthom2s  = symthom2s)
        
    



@get("/login")
def get_login():
    return template("login") 

@get("/adminlogin")
def get_adminlogin():
    return template("adminlogin")

@get("/request")
def get_request():
    return template("request")

@get("/accesspage")
def get_acess():
    return template("accesspage")

@get("/signup")
def get_signup():
    return template("signup")

## gets covid info from index page to be put into 2 tables
#1 table is the private table another if a public table

counter = 0
@post("/index")
def post_info():
    name = request.forms['fullname']
    age = request.forms['age']
    symthom1 = request.forms['symthom1']
    symthom2 = request.forms['symthom2']
    global counter

    #generalizing information
    int_age = int(age)
    general_age =''

    print(type(int_age))

    if counter == 6:
        counter = 0
    ##0-------------------------------
    general_age = k_anonymity(counter, int_age)

    counter = counter + 1

    

    

    

    mycursor.execute("INSERT INTO covidinfo (name, age,symthom1,symthom2) VALUES(%s,%s,%s,%s)", (name,age,symthom1,symthom2))
    mycursor.execute("INSERT INTO publiccovidinfo (name, age,symthom1,symthom2) VALUES(%s,%s,%s,%s)", ('*',general_age,symthom1,symthom2))
    db.commit()
    redirect('/')





@post('/login')
def post_login():
    entered_username = request.forms['username']
    password = request.forms['password']
    try:  mycursor.execute("SELECT username, password from useraccounts WHERE password = " + password + " AND username = " +'"'+entered_username +'"')
    except:  return template('login')
    

    redirect('/useraccount')
    

@post('/adminlogin')
def post_admin_login():
        entered_username = request.forms['username']
        password = request.forms['password']
        try:  mycursor.execute("SELECT username, password from adminaccounts WHERE password = " + password + " AND username = " +'"'+entered_username +'"')
        except:  redirect('/adminlogin')
    
        redirect('/adminpage')


#puts info into request table for admin to see
@post('/request')
def post_request():
    name = request.forms['name']
    email = request.forms['email']
    mycursor.execute("INSERT INTO request (fullname, email) VALUES(%s,%s)", (name,email))
    db.commit()

    redirect('/request')

## sends an email to whoever is granted access
# this is post admin page 
@post('/grant_request')
def post_request():
    request_email = request.forms['email']
    
    adminEmail = "kentprojectemail@gmail.com"
    emailPassword = "kentstate"

    access_code = access_code_generator()    
    message = "access = "+ access_code
    print(access_code)

    mycursor.execute("INSERT INTO accesscodes (accesscode) VALUES(%s)", (access_code,))
    db.commit()

    ## Deletes certain request when granted
    mycursor.execute("DELETE FROM request WHERE email = "+ '"'+ request_email + '"')
    db.commit()
    #print(message)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(adminEmail, emailPassword)
    server.sendmail(adminEmail,request_email, message)

    redirect('/adminpage')

## access code is entered and if entered right user is redirected to signup
@post('/accesspage')
def post_check_access():
    entered_code = request.forms['code']

    try: mycursor.execute("SELECT accesscode from accesscodes WHERE accesscode = "+ '"'+ entered_code + '"')
    except: redirect('/accesspage')
    
    l = []
    for x in mycursor:
        l.append(x)
    
   # x = mycursor.execute("SELECT accesscode from accesscodes WHERE accesscode = "+ '"'+ entered_code + '"')

    mycursor.execute("DELETE FROM accesscodes WHERE accesscode = "+ '"'+ entered_code + '"')
    db.commit()

    if len(l) != 0:
        redirect('/signup')
    else:
        redirect('/accesspage')
        

## enters new account information into useraccounts table
@post('/signup')
def post_signup():
    username = request.forms['username']
    password = request.forms['password']
    name = request.forms['name']
    email = request.forms['email']

    mycursor.execute("INSERT INTO useraccounts (username, password, name ,email) VALUES(%s,%s,%s,%s)", (username,password,name,email))
    db.commit()

    redirect('/login')


run(host="localhost", port=8068)


