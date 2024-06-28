from flask_sqlalchemy import SQLAlchemy
from config import db 

class Users(db.Model) : 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(80), nullable = False)
    pwd = db.Column(db.String(80), nullable = False)
    def to_json(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "email" : self.email,
            "pwd" : self.pwd
                }
class Image(db.Model): 
    belong_to = db.Column(db.Integer, nullable = False)
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Integer, unique = True, nullable = False)
    content = db.Column(db.LargeBinary, nullable = False)

class Writer(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    belong_to = db.Column(db.Integer, nullable = False)
    name = db.Column(db.String(144),nullable = True)
    article = db.Column(db.Text(140))

