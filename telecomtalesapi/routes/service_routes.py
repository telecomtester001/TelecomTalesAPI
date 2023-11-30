from flask import request, jsonify, Response
from telecomtalesapi import app, db
from telecomtalesapi.auth import auth
from telecomtalesapi.models.service import Service
from telecomtalesapi.models.address import Address, address_service
import xmltodict

# Create a new service
@app.route('/services', methods=['POST'])
@auth.login_required
def create_service():
    if is_request_xml():
        data = xmltodict.parse(request.data)['service']
    else:
        data = request.json

    service = Service(**data)
    db.session.add(service)
    db.session.commit()
    return jsonify(service.to_dict()), 201

# Retrieve a specific service
@app.route('/services/<int:service_id>', methods=['GET'])
@auth.login_required
def get_service(service_id):
    service = Service.query.get(service_id)
    if not service:
        return '', 404
    return jsonify(service.to_dict())

# Update a specific service
@app.route('/services/<int:service_id>', methods=['PUT'])
@auth.login_required
def update_service(service_id):
    service = Service.query.get(service_id)
    if not service:
        return '', 404
    
    data = xmltodict.parse(request.data)['service'] if is_request_xml() else request.json
    for key, value in data.items():
        setattr(service, key, value)
    db.session.commit()
    return jsonify(service.to_dict())

# Delete a specific service
@app.route('/services/<int:service_id>', methods=['DELETE'])
@auth.login_required
def delete_service(service_id):
    service = Service.query.get(service_id)
    if not service:
        return '', 404

    db.session.delete(service)
    db.session.commit()
    return '', 204

# Link a service to an address
@app.route('/addresses/<int:address_id>/link_service/<int:service_id>', methods=['POST'])
@auth.login_required
def link_service_to_address(address_id, service_id):
    address = Address.query.get(address_id)
    service = Service.query.get(service_id)
    if not address or not service:
        return jsonify({'message': 'Address or Service not found'}), 404

    address.services.append(service)
    db.session.commit()
    return jsonify({'message': 'Service linked to address successfully'}), 200

def is_request_xml():
    return 'xml' in request.headers.get('Content-Type', '').lower()

# List All Addresses with a Specific Service

@app.route('/services/<int:service_id>/addresses', methods=['GET'])
@auth.login_required
def get_addresses_for_service(service_id):
    service = Service.query.get(service_id)
    if not service:
        return jsonify({'message': 'Service not found'}), 404

    addresses = service.addresses
    return jsonify([address.to_dict() for address in addresses])
