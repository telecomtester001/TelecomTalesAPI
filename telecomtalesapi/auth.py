from werkzeug.security import check_password_hash
from telecomtalesapi.models.user import User
from telecomtalesapi import auth  # Import the auth object from __init__.py

@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
