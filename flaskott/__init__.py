from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = 'AnujPandey15'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

mail = Mail(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager  = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from flaskott import routes
