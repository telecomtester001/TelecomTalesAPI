from telecomtalesapi import db
from .service import address_service  # Import the associative table

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    streetNo = db.Column(db.String(50))
    street = db.Column(db.String(100))
    city = db.Column(db.String(100))
    post = db.Column(db.String(100))
    postNo = db.Column(db.Integer)
    
    # Many-to-many relationship with Service
    services = db.relationship('Service', secondary=address_service, lazy='subquery',
                               backref=db.backref('addresses', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'streetNo': self.streetNo,
            'street': self.street,
            'city': self.city,
            'post': self.post,
            'postNo': self.postNo,
            'services': [{'id': service.id, 'service_name': service.service, 'value': service.value, 'comment': service.comment} 
                         for service in self.services]
        }