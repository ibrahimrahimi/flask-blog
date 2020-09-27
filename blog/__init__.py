from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os


app = Flask(__name__)
bcrypt = Bcrypt(app)

#Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '37796a65dd2d6d4957d197aba95dedc1'

db = SQLAlchemy(app)

from blog import routes

