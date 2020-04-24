from covid19_sim import db, login_manager

# from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

import json

def try_load(value):
    if type(value) is str:
        return json.loads(value)
    else:
        return None

class dbExt():
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Run(db.Model,dbExt):
    __tablename__ = 'runs'
    id = db.Column(db.Integer,primary_key=True)

    users = db.relationship('User')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    name = db.Column(db.Text)
    params = db.Column(db.Text)
    results = db.Column(db.Text)
    selected_time = db.Column(db.Integer)

    # initialization
    def __init__(self,user_id,name,params,results,selected_time):
        self.user_id = user_id
        self.edit(name,params,results,selected_time)
    
    def edit(self, name,params,results,selected_time):
        # self.user_id = user_id
        self.name = name
        self.params = params
        self.results = results
        self.selected_time = selected_time
    
    # db operations
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        
    def update(self,name,params,results,selected_time):
        self.edit(name,params,results,selected_time)
        self.save()

    # output/ representation
    def json(self):
        return {
            'id':self.id,
            'user_id':self.user_id,
            'name' : self.name,
            'params' : try_load(self.params),
            'results' : try_load(self.results),
            'selected_time' : self.selected_time
        }

    def __repr__(self):
        return json.dumps(self.json())



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,dbExt,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String, unique=True, index=True)
    username = db.Column(db.String, unique=True, index=True)
    pw_hash = db.Column(db.String)

    # runs = db.relationship('Run', backref='user', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        # self.pw_hash = 'hello'
        self.pw_hash = generate_password_hash(password)

    def check_password(self,password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        return check_password_hash(self.pw_hash,password)

    def __repr__(self):
        return f"UserName: {self.username}"
