from flask import request, jsonify, Response
from telecomtalesapi import app, db
from telecomtalesapi.auth import auth
from telecomtalesapi.models.service import Service
from telecomtalesapi.models.address import Address, address_service
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
        comment=data['comment']
    ).first()
    if existing_service:
        return Response(xmltodict.unparse({'message': 'Service with these details already exists'}), mimetype='application/xml', status=400) if is_request_xml() else jsonify({'message': 'Service with these details already exists'}), 400

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
        return Response(xmltodict.unparse({'message': 'Service not found'}), mimetype='application/xml', status=404) if is_request_xml() else jsonify({'message': 'Service not found'}), 404
    return Response(xmltodict.unparse({'service': service.to_dict()}), mimetype='application/xml') if is_request_xml() else jsonify(service.to_dict())

# Route for updating a specific service by ID
@app.route('/services/<int:service_id>', methods=['PUT'])
@auth.login_required
def update_service(service_id):
    service = Service.query.get(service_id)
    if not service:
        return Response(xmltodict.unparse({'message': 'Service not found'}), mimetype='application/xml', status=404) if is_request_xml() else jsonify({'message': 'Service not found'}), 404
    
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
        return Response(xmltodict.unparse({'message': 'Service not found'}), mimetype='application/xml', status=404) if is_request_xml() else jsonify({'message': 'Service not found'}), 404

    db.session.delete(service)
    db.session.commit()
    return '', 204

# Route for linking a service to an address
@app.route('/addresses/<int:address_id>/link_service/<int:service_id>', methods=['POST'])
@auth.login_required
def link_service_to_address(address_id, service_id):
    address = Address.query.get(address_id)
    service = Service.query.get(service_id)
    if not address or not service:
        return Response(xmltodict.unparse({'message': 'Address or Service not found'}), mimetype='application/xml', status=404) if is_request_xml() else jsonify({'message': 'Address or Service not found'}), 404

    address.services.append(service)
    db.session.commit()
    return Response(xmltodict.unparse({'message': 'Service linked to address successfully'}), mimetype='application/xml') if is_request_xml() else jsonify({'message': 'Service linked to address successfully'}), 200

# Route for listing all addresses associated with a specific service
@app.route('/services/<int:service_id>/addresses', methods=['GET'])
@auth.login_required
def get_addresses_for_service(service_id):
    service = Service.query.get(service_id)
    if not service:
        return Response(xmltodict.unparse({'message': 'Service not found'}), mimetype='application/xml', status=404) if is_request_xml() else jsonify({'message': 'Service not found'}), 404

    addresses = service.addresses
    return Response(xmltodict.unparse({'addresses': [address.to_dict() for address in addresses]}), mimetype='application/xml') if is_request_xml() else jsonify([address.to_dict() for address in addresses])

# Route for listing all services
@app.route('/services', methods=['GET'])
@auth.login_required
def get_all_services():
    services = Service.query.all()
    return Response(xmltodict.unparse({'services': [service.to_dict() for service in services]}), mimetype='application/xml') if is_request_xml() else jsonify([service.to_dict() for service in services])
