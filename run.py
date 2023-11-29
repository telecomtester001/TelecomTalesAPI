from telecomtalesapi import app, db
from telecomtalesapi.models import *
from flask_migrate import Migrate

# Configure Flask-Migrate
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)  # debug to False for production environment
