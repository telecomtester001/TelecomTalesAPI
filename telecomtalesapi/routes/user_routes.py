from flask_restx import Resource
from telecomtalesapi import user_ns, db
from telecomtalesapi.models.user import User
from telecomtalesapi.schemas import UserSchema
from marshmallow import ValidationError
from flask import request


@user_ns.route('/')  # Define route at the namespace level
class UserList(Resource):
    def post(self):
        """Create a new user."""
        schema = UserSchema()
        try:
            # Validate and deserialize input
            data = schema.load(request.json)
            # Check if user already exists
            if User.query.filter_by(username=data['username']).first():
                return {'message': 'User already exists'}, 400
            
            # Create a new User instance using the validated data
            new_user = User(username=data['username'])
            new_user.set_password(data['password'])
            
            # Add the new user to the database
            db.session.add(new_user)
            db.session.commit()
            
            # Return success message
            return {'message': 'User created successfully'}, 201
        except ValidationError as err:
            return err.messages, 400
