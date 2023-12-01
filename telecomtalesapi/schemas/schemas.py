from marshmallow import Schema, fields, validates, ValidationError, validate
from telecomtalesapi.models.user import User
#from telecomtalesapi.models.address import Address
#from telecomtalesapi.models.service import Service

# Schema for validating Address data
class AddressSchema(Schema):
    streetNo = fields.Str(required=True, validate=validate.Length(max=50))
    street = fields.Str(required=True, validate=validate.Length(max=100))
    city = fields.Str(required=True, validate=validate.Length(max=100))
    post = fields.Str(required=True, validate=validate.Length(max=100))
    postNo = fields.Int(required=True)

    @validates('postNo')
    def validate_postNo(self, value):
        if value <= 0:
            raise ValidationError("Post number must be greater than 0.")

# Schema for validating Service data
class ServiceSchema(Schema):
    service = fields.Str(required=True, validate=validate.Length(max=100))
    value = fields.Bool(required=True)
    comment = fields.Str(validate=validate.Length(max=250))
    address_id = fields.Int(required=True)

    @validates('address_id')
    def validate_address_id(self, value):
        if value <= 0:
            raise ValidationError("Address ID must be greater than 0.")

# Schema for validating User data
class UserSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=3, max=64))
    password = fields.Str(required=True, validate=validate.Length(min=4))

    @validates('username')
    def validate_username(self, value):
        if User.query.filter_by(username=value).first():
            raise ValidationError("Username already exists.")