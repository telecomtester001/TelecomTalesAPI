from flask import request, jsonify, Response
from telecomtalesapi import app, db
from telecomtalesapi.auth import auth
from telecomtalesapi.models.service import Service
import xmltodict

# Helper function to check if request is XML
def is_request_xml():
    return 'xml' in request.headers.get('Content-Type', '').lower()

# Route for creating a new service
@app.route('/services', methods=['POST'])
@auth.login_required
def create_service():
    if is_request_xml():
        data = xmltodict.parse(request.data)['service']
    else:
        data = request.json

    # Check for existing service with the same details
    existing_service = Service.query.filter_by(
        service=data['service'],
        value=data['value'],
        comment=data['comment'],
        address_id=data['address_id']
    ).first()
    if existing_service:
        response_message = {'message': 'Service with these details already exists'}
        return Response(xmltodict.unparse(response_message), mimetype='application/xml', status=400) if is_request_xml() else jsonify(response_message), 400

    service = Service(**data)
    db.session.add(service)
    db.session.commit()
    return Response(xmltodict.unparse({'service': service.to_dict()}), mimetype='application/xml', status=201) if is_request_xml() else jsonify(service.to_dict()), 201

# Route for retrieving a specific service by ID
@app.route('/services/<int:service_id>', methods=['GET'])
@auth.login_required
def get_service(service_id):
    service = Service.query.get(service_id)
    if not service:
        response_message = {'message': 'Service not found'}
        return Response(xmltodict.unparse(response_message), mimetype='application/xml', status=404) if is_request_xml() else jsonify(response_message), 404
    return Response(xmltodict.unparse({'service': service.to_dict()}), mimetype='application/xml') if is_request_xml() else jsonify(service.to_dict())

# Route for updating a specific service by ID
@app.route('/services/<int:service_id>', methods=['PUT'])
@auth.login_required
def update_service(service_id):
    service = Service.query.get(service_id)
    if not service:
        response_message = {'message': 'Service not found'}
        return Response(xmltodict.unparse(response_message), mimetype='application/xml', status=404) if is_request_xml() else jsonify(response_message), 404

    data = xmltodict.parse(request.data)['service'] if is_request_xml() else request.json
    for key, value in data.items():
        setattr(service, key, value)
    db.session.commit()
    return Response(xmltodict.unparse({'service': service.to_dict()}), mimetype='application/xml') if is_request_xml() else jsonify(service.to_dict())

# Route for deleting a specific service by ID
@app.route('/services/<int:service_id>', methods=['DELETE'])
@auth.login_required
def delete_service(service_id):
    service = Service.query.get(service_id)
    if not service:
        response_message = {'message': 'Service not found'}
        return Response(xmltodict.unparse(response_message), mimetype='application/xml', status=404) if is_request_xml() else jsonify(response_message), 404

    db.session.delete(service)
    db.session.commit()
    return '', 204

# Route for listing all services
@app.route('/services', methods=['GET'])
@auth.login_required
def get_all_services():
    services = Service.query.all()
    return Response(xmltodict.unparse({'services': [service.to_dict() for service in services]}), mimetype='application/xml') if is_request_xml() else jsonify([service.to_dict() for service in services])
