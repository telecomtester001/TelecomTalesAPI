
from flask import request, jsonify, Response
from telecomtalesapi import app, db
from telecomtalesapi.auth import auth
from telecomtalesapi.models.address import Address
import xmltodict

@app.route('/addresses', methods=['POST'])
@auth.login_required
def create_address():
    if is_request_xml():
        data = xmltodict.parse(request.data)['address']
    else:
        data = request.json
    address = Address(**data)
    db.session.add(address)
    db.session.commit()
    return jsonify(address.to_dict()), 201

@app.route('/addresses/<int:id>', methods=['GET'])
@auth.login_required
def get_address(id):
    address = Address.query.get(id)
    if not address:
        return '', 404
    return jsonify(address.to_dict())

@app.route('/addresses/<int:id>', methods=['PUT'])
@auth.login_required
def update_address(id):
    address = Address.query.get(id)
    if not address:
        return '', 404
    data = xmltodict.parse(request.data)['address'] if is_request_xml() else request.json
    for key, value in data.items():
        setattr(address, key, value)
    db.session.commit()
    return jsonify(address.to_dict())

@app.route('/addresses/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_address(id):
    address = Address.query.get(id)
    if not address:
        return '', 404
    db.session.delete(address)
    db.session.commit()
    return '', 204

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
    return jsonify([address.to_dict() for address in addresses])

def is_request_xml():
    return 'xml' in request.headers.get('Content-Type', '').lower()

# List All Services for a Specific Address

@app.route('/addresses/<int:address_id>/services', methods=['GET'])
@auth.login_required
def get_services_for_address(address_id):
    address = Address.query.get(address_id)
    if not address:
        return jsonify({'message': 'Address not found'}), 404

    services = address.services
    return jsonify([service.to_dict() for service in services])
