from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b303e689023d5c7e35c1beaed619001d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'  # ' + os.path.join(os.getcwd(), '

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'


from comunidadeimpressionadora import routes