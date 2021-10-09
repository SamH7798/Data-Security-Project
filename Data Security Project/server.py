import mysql.connector
from bottle import route, run, template
from bottle import get, post
from bottle import request

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "dataproject"
    )


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

mycursor = db.cursor()

@route("/")
def get_index():
    return template("index")



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

    mycursor.execute("INSERT INTO covidinfo (name, age,symthom1,symthom2) VALUES(%s,%s,%s,%s)", (anony_name,age,symthom1,symthom2))
    db.commit()


@get("/login")
def get_login():
    return template("login")

run(host="localhost", port=8068)