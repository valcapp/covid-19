from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY']='covid-19'

#########################
##### SQL DATABASE ######
#########################
import os
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.db')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
# db = SQLAlchemy()
# db.init_app(app)
from flask_migrate import Migrate
Migrate(app,db)


###########################
#### LOGIN CONFIGS #######
#########################
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
# Tell users what view to go to when they need to login.
login_manager.login_view = "users.login"


###########################
#### BLUEPRINT CONFIGS #######
#########################
from covid19_sim.core.views import core
from covid19_sim.users.views import users
from covid19_sim.runs.views import runs

# Register the apps
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(runs)

