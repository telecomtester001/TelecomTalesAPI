# Initializes the Flask application

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from config import DevelopmentConfig

# Create the Flask application instance
app = Flask(__name__)

# Load configuration
app.config.from_object(DevelopmentConfig)

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Initialize auth 
auth = HTTPBasicAuth()

# Import models and routes after initializing db 
from telecomtalesapi import models, routes
