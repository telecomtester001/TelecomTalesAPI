import xmltodict

from flask import request, jsonify, Response
from telecomtalesapi import app, db
from telecomtalesapi.auth import auth
from telecomtalesapi.models.service import Service
from telecomtalesapi.schemas import ServiceSchema  
from marshmallow import ValidationError
from ..utils.api_utils import is_request_xml, should_return_xml, to_xml , output_json , output_xml

# Route for creating a new service
@app.route('/services', methods=['POST'])
@auth.login_required
def create_service():
    schema = ServiceSchema()
    try:
        if is_request_xml():
            data = schema.load(xmltodict.parse(request.data)['service'])
        else:
            data = schema.load(request.json)

        existing_service = Service.query.filter_by(**data).first()
        if existing_service:
            response_message = {'message': 'Service with these details already exists'}
            if should_return_xml():
                return output_xml(response_message, 400)
            else:
                return output_json(response_message, 400)

        service = Service(**data)
        db.session.add(service)
        db.session.commit()
        service_data = {'service': service.to_dict()}
        if should_return_xml():
            return output_xml(service_data, 201)
        else:
            return output_json(service_data, 201)
    except ValidationError as err:
        error_message = {'error': err.messages}
        return output_json(error_message, 400) if not should_return_xml() else output_xml(error_message, 400)


# Route for retrieving a specific service by ID
@app.route('/services/<int:service_id>', methods=['GET'])
@auth.login_required
def get_service(service_id):
    service = Service.query.get(service_id)
    if not service:
        response_message = {'message': 'Service not found'}
        if should_return_xml():
            return output_xml(response_message, 404)
        else:
            return output_json(response_message, 404)

    service_data = {'service': service.to_dict()}
    if should_return_xml():
        return output_xml(service_data, 200)
    else:
        return output_json(service_data, 200)

# Route for updating a specific service by ID
@app.route('/services/<int:service_id>', methods=['PUT'])
@auth.login_required
def update_service(service_id):
    service = Service.query.get(service_id)
    if not service:
        response_message = {'message': 'Service not found'}
        if should_return_xml():
            return output_xml(response_message, 404)
        else:
            return output_json(response_message, 404)

    try:
        data = xmltodict.parse(request.data)['service'] if is_request_xml() else request.json
        for key, value in data.items():
            setattr(service, key, value)
        db.session.commit()
        service_data = {'service': service.to_dict()}
        if should_return_xml():
            return output_xml(service_data, 200)
        else:
            return output_json(service_data, 200)
    except Exception as e:
        error_message = {'error': str(e)}
        return output_json(error_message, 400) if not should_return_xml() else output_xml(error_message, 400)


# Route for deleting a specific service by ID
@app.route('/services/<int:service_id>', methods=['DELETE'])
@auth.login_required
def delete_service(service_id):
    service = Service.query.get(service_id)
    if not service:
        response_message = {'message': 'Service not found'}
        if should_return_xml():
            return output_xml(response_message, 404)
        else:
            return output_json(response_message, 404)

    try:
        db.session.delete(service)
        db.session.commit()
        return '', 204
    except Exception as e:
        error_message = {'error': str(e)}
        return output_json(error_message, 500) if not should_return_xml() else output_xml(error_message, 500)


# Route for listing all services
@app.route('/services', methods=['GET'])
@auth.login_required
def get_all_services():
    services = Service.query.all()
    services_data = {'services': [service.to_dict() for service in services]}
    if should_return_xml():
        return output_xml(services_data, 200)
    else:
        return output_json(services_data, 200)
