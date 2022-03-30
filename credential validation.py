import psycopg2
from flask import Flask, make_response, request,jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
cors = CORS(app)
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "testpwd", host = "127.0.0.1", port = "5432")
cur = conn.cursor()


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


@app.route("/user", methods=['POST'])
# function to add and validate new user
def add_user():
    # if request.method == 'POST':
        email_pattern = '^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$'
        password_pattern = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
        req = request.get_json()
        email = req['email']
        password = req['password']
        username = req['username']
        email_result = re.match(email_pattern, email)
        password_result = re.match(password_pattern, password)

        cur.execute("select username, email from credentials where username='{}' and email='{}'".format(username, email))
        rows = cur.fetchone()
        if rows == None:
            if (email_result and password_result):
                cur.execute("insert into credentials (email, password, username) values (%s, %s, %s)", (email, password, username))
                conn.commit()
                res = make_response("User Added", 200)
                return res
            else:
                res = make_response("Invalid Email Address or Password", 400)
                return res
        else:
            res = make_response("Username or Email Already", 400)
            return res       


@app.route("/user", methods=['GET'])
# function to get all users
def get_all_users():
    cur.execute("select * from credentials")
    rows = cur.fetchall()
    data = userdict(rows)
    res = make_response(jsonify(data), 200)
    return res
   

@app.route("/user", methods = ['DELETE'])
# function to delete user
def delete_user():
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
        

@app.route("/user", methods = ['PATCH'])
# function to update password
def change_password():
    req = request.get_json()
    username = req['username']
    password = req['password']
    new_password = req['new_password']
    cur.execute("select * from credentials where password='{0}' and username='{1}'".format(password, username))
    rows = cur.fetchone()
    if rows !=None:
        new_password == password
        cur.execute("update credentials set password='{0}' where username='{1}'".format(new_password, username))
        conn.commit()
        res = make_response("Password Updated", 200)
        return res

    else:
        res = make_response("Invalid Credentials", 400)
        return res     
         

if __name__ == "__main__":
    app.run(debug = True)
    



