
from telecomtalesapi import app, db
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint
from flask import send_from_directory
#from flask import Flask

from telecomtalesapi.models import *

#app = Flask(__name__)  # Create the Flask application instance

# Configure SwaggerUI
SWAGGER_URL = ''  # Expose Swagger UI at the root
API_URL = '/documentation/swagger.yaml'  # API url to the swagger file

# Register the Swagger UI blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Empty string means root
    API_URL,
    config={
        'app_name': "Telecom Tales API"
    },
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/documentation/<path:path>')
def send_documentation(path):
    # Serve files for Swagger UI.
    return send_from_directory('documentation', path)

# Configure Flask-Migrate
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)  # debug to False for production environment