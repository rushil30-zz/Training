from flask import Flask, make_response, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import re

app = Flask(__name__)
cors = CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///credentials.db'
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)


def __init__(self, id, email, username, password):
    self.id = id
    self.email= email
    self.username = username
    self.password = password
    # return '<email %r, username %r, password %r>' % self.id
    return "<(email='%s', username='%s', password='%s')>" % (
            self.email, self.username, self.password)

def datadict(data):
    data_list=[]
    for i in data:
        dic = {}
        dic['id']=i.id
        dic['email']=i.email
        dic['username']=i.username
        dic['password']=i.password
        data_list.append(dic)
    #print(data_list)
    return data_list

@app.route("/user", methods=['POST','GET','DELETE','PATCH'])
def user():
    if request.method == 'POST':
        email_pattern = '^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$'
        password_pattern = '^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
        req = request.get_json()
        email = req['email']
        username = req['username']
        password = req['password']
        email_result = re.match(email_pattern, email)
        password_result = re.match(password_pattern, password)

        if (email_result and password_result):
            req = request.get_json()
            email = req['email']
            username = req['username']
            password = req['password']
            # email = request.form['email']
            # username = request.form['username']
            # password = request.form['password']
            db.session.add(email, username, password)
            db.session.commit()
            res = make_response("User Added", 201)
            return res
        else:
            res = make_response("Invalid Email Address or Password", 400)
            return res


    if request.method == 'GET':
        data = Users.query.all()
        data = datadict(data)
        res = make_response(jsonify(data), 200)
        return res  


    if request.method == 'DELETE':
        user_to_delete = Users.query.get_or_404(id)
        try:
            db.session.delete(user_to_delete)
            db.session.commit()
            res = make_response("User Deleted", 200)
            return res
        except:
            res = make_response("Error while deleting user", 404)
            return res


    # if request.method == 'PATCH':


if __name__ == '__main__':
    db.create_all()
app.run(debug = True)