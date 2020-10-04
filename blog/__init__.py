import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
import pdb
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

#Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '37796a65dd2d6d4957d197aba95dedc1'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ibrahim.rahimi.dev@gmail.com'
app.config['MAIL_PASSWORD'] = '3030@Irizal' 
mail = Mail(app)

db = SQLAlchemy(app)

from blog import routes

