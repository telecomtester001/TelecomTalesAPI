
from flask import request, jsonify, Response
from telecomtalesapi import app, db
from telecomtalesapi.auth import auth
from telecomtalesapi.models.service import Service
from telecomtalesapi.models.address import Address
import xmltodict

@app.route('/addresses/<int:address_id>/services', methods=['POST'])
@auth.login_required
def add_service(address_id):
    address = Address.query.get(address_id)
    if not address:
        return jsonify({'message': 'Address not found'}), 404

    if is_request_xml():
        data = xmltodict.parse(request.data)['service']
    else:
        data = request.json

    service = Service(address_id=address_id, **data)
    db.session.add(service)
    db.session.commit()
    return jsonify(service.to_dict()), 201

@app.route('/addresses/<int:address_id>/services/<int:service_id>', methods=['GET'])
@auth.login_required
def get_service(address_id, service_id):
    service = Service.query.filter_by(id=service_id, address_id=address_id).first()
    if not service:
        return '', 404
    return jsonify(service.to_dict())

@app.route('/addresses/<int:address_id>/services/<int:service_id>', methods=['PUT'])
@auth.login_required
def update_service(address_id, service_id):
    service = Service.query.filter_by(id=service_id, address_id=address_id).first()
    if not service:
        return '', 404

    data = xmltodict.parse(request.data)['service'] if is_request_xml() else request.json
    for key, value in data.items():
        setattr(service, key, value)
    db.session.commit()
    return jsonify(service.to_dict())

@app.route('/addresses/<int:address_id>/services/<int:service_id>', methods=['DELETE'])
@auth.login_required
def delete_service(address_id, service_id):
    service = Service.query.filter_by(id=service_id, address_id=address_id).first()
    if not service:
        return '', 404

    db.session.delete(service)
    db.session.commit()
    return '', 204

def is_request_xml():
    return 'xml' in request.headers.get('Content-Type', '').lower()

