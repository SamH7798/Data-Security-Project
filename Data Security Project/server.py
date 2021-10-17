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

@post("/index")
def post_info():
    name = request.forms['fullname']
    age = request.forms['age']
    symthom1 = request.forms['symthom1']
    symthom2 = request.forms['symthom2']
    
    anony_name = ""
    count = 0
    for x in name:
        count = count + 1

    for x in range(count):
       anony_name = anony_name + '*'

    mycursor.execute("INSERT INTO covidinfo (name, age,symthom1,symthom2) VALUES(%s,%s,%s,%s)", (name,age,symthom1,symthom2))
    mycursor.execute("INSERT INTO publiccovidinfo (name, age,symthom1,symthom2) VALUES(%s,%s,%s,%s)", (anony_name,age,symthom1,symthom2))
    db.commit()





@post('/login')
def post_login():
    entered_username = request.forms['username']
    password = request.forms['password']
    try:  mycursor.execute("SELECT username, password from useraccounts WHERE password = " + password + " AND username = " +'"'+entered_username +'"')
    except:  redirect('/')
    
    redirect('/useraccount')
    

@post('/adminlogin')
def post_admin_login():
        entered_username = request.forms['username']
        password = request.forms['password']
        try:  mycursor.execute("SELECT username, password from adminaccounts WHERE password = " + password + " AND username = " +'"'+entered_username +'"')
        except:  redirect('/')
    
        redirect('/adminpage')



@post('/request')
def post_request():
    print("hello")
    name = request.forms['name']
    email = request.forms['email']
    mycursor.execute("INSERT INTO request (fullname, email) VALUES(%s,%s)", (name,email))
    db.commit()

    redirect('/request')


@post('/grant_request')
def post_request():
    request_email = request.forms['email']
    
    adminEmail = "kentprojectemail@gmail.com"
    emailPassword = ""

    access_code = access_code_generator()    
    message = "access = "+ access_code
    print(access_code)

    mycursor.execute("INSERT INTO accesscodes (accesscode) VALUES(%s)", (access_code,))
    db.commit()

    ## remeber to delete granted request

    #print(message)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(adminEmail, emailPassword)
    server.sendmail(adminEmail,request_email, message)

    redirect('/adminpage')

@post('/accesspage')
def post_check_access():
    entered_code = request.forms['code']
    print(entered_code)

    try:  mycursor.execute("SELECT accesscode from accesscodes WHERE accesscode = "+ '"'+ entered_code + '"')
    except:  redirect('/accesspage')
    print(entered_code)

    mycursor.execute("DELETE FROM accesscodes WHERE accesscode = "+ '"'+ entered_code + '"')
    db.commit()

    redirect('/signup')

   
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
