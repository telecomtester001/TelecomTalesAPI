from flask_restx import Resource
from flask_restx import fields
from flask import Response
from flask import request, jsonify
from telecomtalesapi import service_ns
from telecomtalesapi import db
from telecomtalesapi.models.service import Service
from telecomtalesapi.schemas import ServiceSchema
from marshmallow import ValidationError
import xmltodict
from telecomtalesapi.auth import auth
from ..utils.api_utils import is_request_xml, should_return_xml, to_xml

service_model = service_ns.model('Service', {
    'service': fields.String(required=True, description='The service name'),
    'value': fields.Boolean(required=True, description='The status of service'),
    'comment': fields.String(required=True, description='The comment for this specific service'),
    'address_id': fields.Integer(required=True, description='Address id to wich this service is linked'),
})


@service_ns.route('/')  # Define route at the namespace level
class ServiceList(Resource):
    @auth.login_required
    def get(self):
        # Retrieve all services
        services = Service.query.all()
        return jsonify([service.to_dict() for service in services])

    @auth.login_required
    @service_ns.expect(service_model, validate=True)
    def post(self):
        # Create a new service
        schema = ServiceSchema()
        try:
            if is_request_xml():
                data = schema.load(xmltodict.parse(request.data)['service'])
            else:
                data = schema.load(request.json)

            existing_service = Service.query.filter_by(**data).first()
            if existing_service:
                return {'message': 'Service with these details already exists'}, 400

            service = Service(**data)
            db.session.add(service)
            db.session.commit()
            return service.to_dict(), 201
        except ValidationError as err:
            return err.messages, 400

@service_ns.route('/<int:service_id>')  # Route for specific service by ID
class ServiceResource(Resource):
    @auth.login_required
    def get(self, service_id):
        # Get a specific service by ID
        service = Service.query.get(service_id)
        if not service:
            return {'message': 'Service not found'}, 404
        return service.to_dict()

    @auth.login_required
    @service_ns.expect(service_model, validate=True)
    def put(self, service_id):
        # Update a specific service by ID
        schema = ServiceSchema(partial=True)
        service = Service.query.get(service_id)
        if not service:
            return {'message': 'Service not found'}, 404

        try:
            data = schema.load(request.json) if not is_request_xml() else xmltodict.parse(request.data)['service']
            for key, value in data.items():
                setattr(service, key, value)
            db.session.commit()
            return service.to_dict(), 200
        except ValidationError as err:
            return err.messages, 400

    @auth.login_required
    def delete(self, service_id):
        # Delete a specific service by ID
        service = Service.query.get(service_id)
        if not service:
            return {'message': 'Service not found'}, 404
        db.session.delete(service)
        db.session.commit()
        return '', 204
