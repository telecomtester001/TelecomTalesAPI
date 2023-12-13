import xmltodict
from telecomtalesapi import app, db
from telecomtalesapi.models.user import User
from telecomtalesapi.schemas import UserSchema
from flask import request
from marshmallow import ValidationError
from ..utils.api_utils import is_request_xml, should_return_xml , output_json , output_xml

@app.route('/create_user', methods=['POST'])
def create_user():
    schema = UserSchema()
    try:
        # Handling both XML and JSON requests
        if is_request_xml():
            data = schema.load(xmltodict.parse(request.data)['User'])
        else:
            data = schema.load(request.json)
    except ValidationError as err:
        # Send error in requested format
        error_message = {'error': err.messages}
        return output_json(error_message, 400) if not should_return_xml() else output_xml(error_message, 400)

    # Check if user already exists
    if User.query.filter_by(username=data['username']).first():
        response_message = {'message': 'User already exists'}
        if should_return_xml():
            return output_xml(response_message, 400)
        else:
            return output_json(response_message, 400)
    
    # Create and save the new user
    new_user = User(username=data['username'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    
    # Return success message in requested format
    success_message = {'message': 'User created successfully'}
    if should_return_xml():
        return output_xml(success_message, 201)
    else:
        return output_json(success_message, 201)