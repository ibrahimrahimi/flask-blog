from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '37796a65dd2d6d4957d197aba95dedc1'
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from blog import routes

