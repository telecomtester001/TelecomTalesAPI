from flask import request, jsonify, Response
from telecomtalesapi import app, db
from telecomtalesapi.auth import auth
from telecomtalesapi.models.address import Address
import xmltodict

# Helper function to check if request is XML
def is_request_xml():
    return 'xml' in request.headers.get('Content-Type', '').lower()

# Create Address Route

@app.route('/addresses', methods=['POST'])
@auth.login_required
def create_address():
    if is_request_xml():
        data = xmltodict.parse(request.data)['address']
    else:
        data = request.json

    # Check for existing address with the same details
    existing_address = Address.query.filter_by(
        streetNo=data['streetNo'],
        street=data['street'],
        city=data['city'],
        post=data['post'],
        postNo=data['postNo']
    ).first()

    if existing_address:
        return Response(xmltodict.unparse({'message': 'Address with these details already exists'}), mimetype='application/xml', status=400) if is_request_xml() else jsonify({'message': 'Address with these details already exists'}), 400

    address = Address(**data)
    db.session.add(address)
    db.session.commit()
    return Response(xmltodict.unparse({'address': address.to_dict()}), mimetype='application/xml', status=201) if is_request_xml() else jsonify(address.to_dict()), 201

# Get Address by ID Route

@app.route('/addresses/<int:id>', methods=['GET'])
@auth.login_required
def get_address(id):
    address = Address.query.get(id)
    if not address:
        return Response(xmltodict.unparse({'message': 'Address not found'}), mimetype='application/xml', status=404) if is_request_xml() else jsonify({'message': 'Address not found'}), 404
    return Response(xmltodict.unparse({'address': address.to_dict()}), mimetype='application/xml') if is_request_xml() else jsonify(address.to_dict())

# Update Address Route

@app.route('/addresses/<int:id>', methods=['PUT'])
@auth.login_required
def update_address(id):
    address = Address.query.get(id)
    if not address:
        return Response(xmltodict.unparse({'message': 'Address not found'}), mimetype='application/xml', status=404) if is_request_xml() else jsonify({'message': 'Address not found'}), 404

    data = xmltodict.parse(request.data)['address'] if is_request_xml() else request.json
    for key, value in data.items():
        setattr(address, key, value)
    db.session.commit()
    return Response(xmltodict.unparse({'address': address.to_dict()}), mimetype='application/xml') if is_request_xml() else jsonify(address.to_dict())

# Delete Address Route

@app.route('/addresses/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_address(id):
    address = Address.query.get(id)
    if not address:
        return Response(xmltodict.unparse({'message': 'Address not found'}), mimetype='application/xml', status=404) if is_request_xml() else jsonify({'message': 'Address not found'}), 404
    db.session.delete(address)
    db.session.commit()
    return '', 204

# Query Addresses Route 

@app.route('/addresses/query', methods=['GET'])
@auth.login_required
def query_addresses():
    city = request.args.get('city')
    post_no = request.args.get('postNo')
    query = Address.query
    if city:
        query = query.filter(Address.city == city)
    if post_no:
        query = query.filter(Address.postNo == post_no)
    addresses = query.all()
    return Response(xmltodict.unparse({'addresses': [address.to_dict() for address in addresses]}), mimetype='application/xml') if is_request_xml() else jsonify([address.to_dict() for address in addresses])

# List Services for an Address Route

@app.route('/addresses/<int:address_id>/services', methods=['GET'])
@auth.login_required
def get_services_for_address(address_id):
    address = Address.query.get(address_id)
    if not address:
        return Response(xmltodict.unparse({'message': 'Address not found'}), mimetype='application/xml', status=404) if is_request_xml() else jsonify({'message': 'Address not found'}), 404
    services = address.services
    return Response(xmltodict.unparse({'services': [service.to_dict() for service in services]}), mimetype='application/xml') if is_request_xml() else jsonify([service.to_dict() for service in services])

# List All Addresses Route

@app.route('/addresses', methods=['GET'])
@auth.login_required
def get_all_addresses():
    addresses = Address.query.all()
    return Response(xmltodict.unparse({'addresses': [address.to_dict() for address in addresses]}), mimetype='application/xml') if is_request_xml() else jsonify([address.to_dict() for address in addresses])
