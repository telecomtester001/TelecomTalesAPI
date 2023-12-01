from telecomtalesapi import app, db
from telecomtalesapi.models.user import User
from telecomtalesapi.schemas import UserSchema
from flask import request, jsonify
from marshmallow import ValidationError

@app.route('/create_user', methods=['POST'])
def create_user():
     # Instantiate the UserSchema
    schema = UserSchema()
    try:
        # Validate and deserialize input
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Check if user already exists
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'User already exists'}), 400
    
    # Create a new User instance using the validated data
    new_user = User(username=data['username'])
    new_user.set_password(data['password'])
    
    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    
    # Return success message
    return jsonify({'message': 'User created successfully'}), 201
