import pdb
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from blog.config import Config
from flask_migrate import Migrate

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'

mail = Mail()
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    with app.app_context():
        db.init_app(app)
        
        migrate.init_app(app, db)
        bcrypt.init_app(app)
        login_manager.init_app(app)
        mail.init_app(app)    

    from blog.user.routes import user
    from blog.post.routes import post
    from blog.main.routes import main
    app.register_blueprint(user)
    app.register_blueprint(post)
    app.register_blueprint(main)
    return app
