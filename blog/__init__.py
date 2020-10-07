import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from blog.config import Config


app = Flask(__name__)
app.config.from_object(Config)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'

mail = Mail(app)

db = SQLAlchemy(app)


from blog.user.routes import user
from blog.post.routes import post
from blog.main.routes import main

app.register_blueprint(user)
app.register_blueprint(post)
app.register_blueprint(main)