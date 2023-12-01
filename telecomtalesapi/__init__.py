# Initializes the Flask application

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from config import DevelopmentConfig

app = Flask(__name__)  # Create the Flask application instance
app.config.from_object(DevelopmentConfig)  # Load configuration

db = SQLAlchemy(app)  # Initialize SQLAlchemy with the Flask app
auth = HTTPBasicAuth()  # Initialize auth

from .auth import verify_password  # Importing auth-related functions

from .schemas import AddressSchema, ServiceSchema, UserSchema # Import schemas

# Import routes
from .routes.address_routes import *
from .routes.service_routes import *
from .routes.user_routes import *
