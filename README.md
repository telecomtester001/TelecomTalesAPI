# TelecomTalesAPI

## Introduction
TelecomTalesAPI is a RESTful API developed using Flask for managing telecom services. It's designed as a lightweight solution for simulating telecommunication operator services.

## Features
- CRUD operations for Address and Service entities.
- Support for both JSON and XML data formats.
- Basic authentication.
- SQLite database integration.

## Setup Instructions

### Prerequisites
- Python 3
- pip (Python package installer)

### Installing Dependencies

1. **pip Installation**
   ```bash
   sudo apt install python3-pip

2. **Flask and Related Libraries**
   ```bash
   pip install Flask Flask-RESTful Flask-SQLAlchemy flask-httpauth Flask-Migrate

3. **Werkzeug Library**
   ```bash
   pip install Werkzeug

## Using Using requirements.txt

0. **To install all dependencies at once:**
   ```bash
   pip install -r requirements.txt


### Set up the database:
4. **Set up the database:**
   ```bash
   export FLASK_APP=run.py
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade

### Starting the Application:
5. **to start the application, run:**
   ```bash
   python run.py

## API Testing Tool

5. **Postman**
   ```bash
   snap install postman

## Scripts

6. **To use scripts install requests library**
   ```bash
   pip install requests

## Navigate to script folder and run script 

6. **To use script run paython script_name.py**
   ```bash
   python create_user_script.py
   python create_address_script.py
   python create_service_script.py
   python delete_address_script.py
   python delete_service_script.py
   python get_address_script.py
   python get_service_script.py
   python link_service_to_address_script.py
   python query_addresses_script.py
   python update_address_script.py
   python update_service_script.py

## Docker Implementation

### TODO
