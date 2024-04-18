from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///School.db"
app.config["SQLALCHEYMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "TechPioneer"
db = SQLAlchemy(app)