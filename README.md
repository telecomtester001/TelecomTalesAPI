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

## API Testing Tool

5. **Postman**
   ```bash
   snap install postman

## Docker Implementation

### TODO
