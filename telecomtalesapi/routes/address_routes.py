import xmltodict

from flask import request, jsonify, Response
from telecomtalesapi import app, db
from telecomtalesapi.auth import auth
from telecomtalesapi.models.address import Address
from telecomtalesapi.schemas import AddressSchema  
from marshmallow import ValidationError
from ..utils.api_utils import is_request_xml, should_return_xml, to_xml , output_json , output_xml

# Route to create a new address
@app.route('/addresses', methods=['POST'])
@auth.login_required
def create_address():
    schema = AddressSchema()
    try:
        if is_request_xml():
            data = schema.load(xmltodict.parse(request.data)['address'])
        else:
            data = schema.load(request.json)

        existing_address = Address.query.filter_by(**data).first()
        if existing_address:
            response_message = {'message': 'Address with these details already exists'}
            if should_return_xml():
                return output_xml(response_message, 400)
            else:
                return output_json(response_message, 400)

        address = Address(**data)
        db.session.add(address)
        db.session.commit()
        address_data = {'address': address.to_dict()}
        if should_return_xml():
            return output_xml(address_data, 201)
        else:
            return output_json(address_data, 201)
    except ValidationError as err:
        return output_json(err.messages, 400) if not should_return_xml() else output_xml({'error': err.messages}, 400)


# Route to get an address by its ID
@app.route('/addresses/<int:id>', methods=['GET'])
@auth.login_required
def get_address(id):
    address = Address.query.get(id)
    if not address:
        response_message = {'message': 'Address not found'}
        if should_return_xml():
            return output_xml(response_message, 404)
        else:
            return output_json(response_message, 404)

    address_data = {'address': address.to_dict()}
    if should_return_xml():
        return output_xml(address_data, 200)
    else:
        return output_json(address_data, 200)
    
# Route to get addresses by city
@app.route('/addresses/city', methods=['GET'])
@auth.login_required
def get_addresses_by_city():
    city = request.args.get('city')
    if not city:
        return jsonify({'message': 'City parameter is required'}), 400

    addresses = Address.query.filter_by(city=city).all()
    if not addresses:
        response_message = {'message': 'No addresses found for the specified city'}
        if should_return_xml():
            return output_xml(response_message, 404)
        else:
            return output_json(response_message, 404)

    addresses_data = {'addresses': [address.to_dict() for address in addresses]}
    if should_return_xml():
        return output_xml(addresses_data, 200)
    else:
        return output_json(addresses_data, 200)

# Route to get addresses by street

@app.route('/addresses/street', methods=['GET'])
@auth.login_required
def get_addresses_by_street():
    street = request.args.get('street')
    if not street:
        return jsonify({'message': 'Street parameter is required'}), 400

    addresses = Address.query.filter_by(street=street).all()
    if not addresses:
        response_message = {'message': 'No addresses found for the specified street'}
        if should_return_xml():
            return output_xml(response_message, 404)
        else:
            return output_json(response_message, 404)

    addresses_data = {'addresses': [address.to_dict() for address in addresses]}
    if should_return_xml():
        return output_xml(addresses_data, 200)
    else:
        return output_json(addresses_data, 200)


# Route to update an existing address
@app.route('/addresses/<int:id>', methods=['PUT'])
@auth.login_required
def update_address(id):
    address = Address.query.get(id)
    if not address:
        response_message = {'message': 'Address not found'}
        if should_return_xml():
            return output_xml(response_message, 404)
        else:
            return output_json(response_message, 404)

    try:
        data = xmltodict.parse(request.data)['address'] if is_request_xml() else request.json
        for key, value in data.items():
            setattr(address, key, value)
        db.session.commit()
        address_data = {'address': address.to_dict()}
        if should_return_xml():
            return output_xml(address_data, 200)
        else:
            return output_json(address_data, 200)
    except Exception as e:
        error_message = {'error': str(e)}
        return output_json(error_message, 400) if not should_return_xml() else output_xml(error_message, 400)

# Route to delete an existing address
@app.route('/addresses/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_address(id):
    address = Address.query.get(id)
    if not address:
        response_message = {'message': 'Address not found'}
        if should_return_xml():
            return output_xml(response_message, 404)
        else:
            return output_json(response_message, 404)

    try:
        db.session.delete(address)
        db.session.commit()
        return '', 204
    except Exception as e:
        error_message = {'error': str(e)}
        return output_json(error_message, 500) if not should_return_xml() else output_xml(error_message, 500)


# Route to query addresses based on certain criteria like city or post number
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

    if not addresses:
        response_message = {'message': 'No addresses found'}
        if should_return_xml():
            return output_xml(response_message, 404)
        else:
            return output_json(response_message, 404)

    addresses_data = {'addresses': [address.to_dict() for address in addresses]}
    if should_return_xml():
        return output_xml(addresses_data, 200)
    else:
        return output_json(addresses_data, 200)

# Route to list services for a specific address
@app.route('/addresses/<int:address_id>/services', methods=['GET'])
@auth.login_required
def get_services_for_address(address_id):
    address = Address.query.get(address_id)
    if not address:
        response_message = {'message': 'Address not found'}
        if should_return_xml():
            return output_xml(response_message, 404)
        else:
            return output_json(response_message, 404)

    services_data = {'services': [service.to_dict() for service in address.services]}
    if should_return_xml():
        return output_xml(services_data, 200)
    else:
        return output_json(services_data, 200)
    
# Route to list all addresses
@app.route('/addresses', methods=['GET'])
@auth.login_required
def get_all_addresses():
    addresses = Address.query.all()
    addresses_data = {'addresses': [address.to_dict() for address in addresses]}
    if should_return_xml():
        return output_xml(addresses_data, 200)
    else:
        return output_json(addresses_data, 200)