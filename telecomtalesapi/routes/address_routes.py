from flask_restx import Resource
from telecomtalesapi import address_ns
from telecomtalesapi import db
from telecomtalesapi.models.address import Address
from telecomtalesapi.schemas import AddressSchema
from marshmallow import ValidationError
from flask import request, jsonify
import xmltodict
from telecomtalesapi.auth import auth

# Helper function to check if request is XML
def is_request_xml():
    return 'xml' in request.headers.get('Content-Type', '').lower()

@address_ns.route('/')  # Define route at the namespace level
class AddressList(Resource):
    @auth.login_required
    def get(self):
        # Retrieve all addresses
        addresses = Address.query.all()
        return jsonify([address.to_dict() for address in addresses])

    @auth.login_required
    def post(self):
        # Create a new address
        schema = AddressSchema()
        try:
            if is_request_xml():
                data = schema.load(xmltodict.parse(request.data)['address'])
            else:
                data = schema.load(request.json)

            existing_address = Address.query.filter_by(**data).first()
            if existing_address:
                return {'message': 'Address with these details already exists'}, 400

            address = Address(**data)
            db.session.add(address)
            db.session.commit()
            return address.to_dict(), 201
        except ValidationError as err:
            return err.messages, 400

@address_ns.route('/<int:id>')  # Route for specific address by ID
class AddressResource(Resource):
    @auth.login_required
    def get(self, id):
        # Get a specific address by ID
        address = Address.query.get(id)
        if not address:
            return {'message': 'Address not found'}, 404
        return address.to_dict()

    @auth.login_required
    def put(self, id):
        # Update a specific address by ID
        schema = AddressSchema(partial=True)
        address = Address.query.get(id)
        if not address:
            return {'message': 'Address not found'}, 404

        try:
            data = schema.load(request.json) if not is_request_xml() else xmltodict.parse(request.data)['address']
            for key, value in data.items():
                setattr(address, key, value)
            db.session.commit()
            return address.to_dict(), 200
        except ValidationError as err:
            return err.messages, 400

    @auth.login_required
    def delete(self, id):
        # Delete a specific address by ID
        address = Address.query.get(id)
        if not address:
            return {'message': 'Address not found'}, 404
        db.session.delete(address)
        db.session.commit()
        return '', 204

@address_ns.route('/query')  # Route for querying addresses
class AddressQuery(Resource):
    @auth.login_required
    def get(self):
        # Query addresses based on request arguments
        args = request.args
        query = Address.query
        for key, value in args.items():
            if hasattr(Address, key):
                query = query.filter(getattr(Address, key) == value)
        addresses = query.all()
        return jsonify([address.to_dict() for address in addresses])

@address_ns.route('/<int:address_id>/services')  # Route for listing services of a specific address
class AddressServices(Resource):
    @auth.login_required
    def get(self, address_id):
        # Retrieve services linked to a specific address
        address = Address.query.get(address_id)
        if not address:
            return {'message': 'Address not found'}, 404
        services = address.services.all()
        return jsonify([service.to_dict() for service in services])
