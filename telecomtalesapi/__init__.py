# Initializes the Flask application

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
from config import DevelopmentConfig

app = Flask(__name__)  # Create the Flask application instance
app.config.from_object(DevelopmentConfig)  # Load configuration

db = SQLAlchemy(app)  # Initialize SQLAlchemy with the Flask app
migrate = Migrate(app, db)
CORS(app)# Enable CORS for all routes
auth = HTTPBasicAuth()  # Initialize auth


# Import models and routes after the app and extensions have been initialized
from .models import *
from .routes import *

from .auth import verify_password  # Importing auth-related functions

from .schemas import AddressSchema, ServiceSchema, UserSchema # Import schemas

# Import routes
from .routes.address_routes import *
from .routes.service_routes import *
from .routes.user_routes import *
