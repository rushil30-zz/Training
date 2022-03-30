import os
from dotenv import load_dotenv
import psycopg2
from flask import Flask, make_response, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
cors = CORS(app)
load_dotenv()
database = os.getenv('DATABASE')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
port = os.getenv('PORT')

conn = psycopg2.connect(database = database, user = user, password = password, host = host, port = port)
cur = conn.cursor()
cur.execute("select * from credentials")
data = cur.fetchall()


def userdict(data):
    user_list=[]
    for i in data:
        dic={}
        dic['id'] = i[0]
        dic['email'] = i[1] 
        dic['username'] = i[2]
        dic['password'] = i[3]      
        user_list.append(dic)
    return user_list


@app.route("/user", methods=['POST','GET','DELETE','PATCH'])
def user():
    # to add and validate new user
    if request.method == 'POST':
        email_pattern = '^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$'
        password_pattern = '^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
        req = request.get_json()
        email = req['email']
        username = req['username']
        password = req['password']
        email_result = re.match(email_pattern, email)
        password_result = re.match(password_pattern, password)

        cur.execute("select username, email, password from credentials where username='{}' or email='{}' or password='{}'".format(username, email, password))
        rows = cur.fetchone()
        if rows == None:
            if (email_result and password_result):
                cur.execute("insert into credentials (email, password, username) values (%s, %s, %s)", (email, password, username))
                conn.commit()
                res = make_response("User Added", 201)
                return res
            else:
                res = make_response("Invalid Email Address or Password", 400)
                return res
        else:
            res = make_response("Credentials already exists", 400)
            return res   

# to get all users
    if request.method == 'GET':
        cur.execute("select * from credentials")
        rows = cur.fetchall()
        data = userdict(rows)
        res = make_response(jsonify(data), 200)
        return res

# to delete a user
    if request.method == 'DELETE': 
        req = request.get_json()
        email = req['email']
        password = req['password']
        username = req['username']
        cur.execute("select * from credentials where email='{0}' and password='{1}' and username='{2}'".format(email, password, username))
        rows = cur.fetchone()
        if rows != None:
            cur.execute("delete from credentials where email='{0}' and password='{1}' and username='{2}'".format(email, password, username))
            conn.commit()
            res = make_response("User Deleted", 200)
            return res
        else:
            res = make_response("Invalid Credentials", 400)
            return res  

# to update password
    if request.method =='PATCH':
        req = request.get_json()
    username = req['username']
    password = req['password']
    new_password = req['new_password']
    # cur.execute("select * from credentials where password='{0}' and username='{1}'".format(password, username))
    cur.execute("select id from credentials where password='{0}' and username='{1}'".format(password, username))
    rows = cur.fetchone()
    if rows !=None:
        new_password == password
        #cur.execute("update credentials set password='{0}' where username='{1}'".format(new_password, username))
        cur.execute("update credentials set password='{0}' where id='{1}'".format(new_password, rows[0]))
        conn.commit()
        res = make_response("Password Updated", 200)
        return res
    else:
        res = make_response("Invalid Credentials", 400)
        return res      
         

if __name__ == "__main__":
    app.run(debug = True)




