from flask_restx import Resource
from telecomtalesapi import user_ns, db
from telecomtalesapi.models.user import User
from telecomtalesapi.schemas import UserSchema
from marshmallow import ValidationError
from flask import request
import xmltodict
from ..utils.api_utils import is_request_xml, should_return_xml, to_xml

@user_ns.route('/')  # Define route at the namespace level
class UserList(Resource):
    def post(self):
        """Create a new user."""
        schema = UserSchema()
        try:
            # Check if the request is XML or JSON and validate accordingly
            if is_request_xml():
                data = schema.load(xmltodict.parse(request.data)['user'])
            else:
                data = schema.load(request.json)

            # Check if user already exists
            if User.query.filter_by(username=data['username']).first():
                error_message = {'message': 'User already exists'}
                if should_return_xml():
                    return to_xml(error_message), 400, {'Content-Type': 'application/xml'}
                else:
                    return error_message, 400

            # Create a new User instance using the validated data
            new_user = User(username=data['username'])
            new_user.set_password(data['password'])

            # Add the new user to the database
            db.session.add(new_user)
            db.session.commit()

            # Return success message
            success_message = {'message': 'User created successfully'}
            if should_return_xml():
                return to_xml(success_message), 201, {'Content-Type': 'application/xml'}
            else:
                return success_message, 201
        except ValidationError as err:
            # Return errors
            if should_return_xml():
                return to_xml({'error': err.messages}), 400, {'Content-Type': 'application/xml'}
            else:
                return err.messages, 400