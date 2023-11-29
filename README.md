# TelecomTalesAPI
RESTful API for managing telecom services using Flask. 
Features CRUD operations for Address and Service entities, supports both JSON and XML data formats, and includes basic authentication and SQLite database integration. 
Designed as a lightweight solution for simulating telecommunication operator services.



setup steps

Installing pip
command:
sudo apt install python3-pip


Installing flask
command:
pip install Flask
pip install Flask-RESTful
pip install Flask-SQLAlchemy
pip install flask flask-httpauth 
pip install Flask-Migrate

Werkzeug library install
command:

pip install Werkzeug



Integrating a Database

To integrate a database into Flask application, we use Flask-SQLAlchemy
command:
pip install Flask-SQLAlchemy

Api Testing Tool 
Postman 

command:
snap install postman

Once models are created we use them to setup the database.

Install Flask-Migrate
command:
pip install Flask-Migrate



------------------------------------------------
Integrated requirements inside requirements.txt
------------------------------------------------

to install them run:

pip install -r requirements.txt



-------------


To setup the database based on the models run this commands in root of the project:

export FLASK_APP=run.py
flask db init
flask db migrate -m "Initial migration."
flask db upgrade

be sure that "migrations" folder is empty prior to running this commands 


Docker implementation

------

TODO