from flask import Flask
from .site.routes import site
from .api.routes import api
from .authentication.routes import auth
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# imports from models
from .models import db as root_db, login_manager, ma
# Import Flask-Marshmallow
from flask_marshmallow import Marshmallow

# Flask-Cors Import
from flask_cors import CORS

# Grab JSONEncoder from Helpers
from marvel_api.helpers import JSONEncoder

app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(api)
app.register_blueprint(auth)



app.config.from_object(Config)

root_db.init_app(app)
#order matters
migrate = Migrate(app, root_db)
login_manager.init_app(app)
login_manager.login_view = 'auth.signin'

ma.init_app(app)

app.json_encoder = JSONEncoder

CORS(app)