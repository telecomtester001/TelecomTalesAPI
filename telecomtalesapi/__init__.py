# Initializes the Flask application

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from config import DevelopmentConfig
from flask_restx import Api, Namespace

app = Flask(__name__)  # Create the Flask application instance
app.config.from_object(DevelopmentConfig)  # Load configuration

db = SQLAlchemy(app)  # Initialize SQLAlchemy with the Flask app
auth = HTTPBasicAuth()  # Initialize auth
api = Api(app) # Initialize Flask-RESTX Api

# Create namespaces
address_ns = Namespace('addresses', description='Address related operations')
service_ns = Namespace('services', description='Service related operations')
user_ns = Namespace('users', description='User related operations') 

# Add namespaces to the API
api.add_namespace(address_ns)
api.add_namespace(service_ns)
api.add_namespace(user_ns)

from .schemas import AddressSchema, ServiceSchema, UserSchema # Import schemas

# Import routes
from .routes.address_routes import *
from .routes.service_routes import *
from .routes.user_routes import *
