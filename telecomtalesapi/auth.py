from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash
from telecomtalesapi.models.user import User

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    # Retrieve user from the database
    user = User.query.filter_by(username=username).first()
    if not user:
        return False  # user not found
    # Check the password hash
    return check_password_hash(user.password_hash, password)
