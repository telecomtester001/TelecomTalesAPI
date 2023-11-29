from telecomtalesapi import db

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    streetNo = db.Column(db.String(50))
    street = db.Column(db.String(100))
    city = db.Column(db.String(100))
    post = db.Column(db.String(100))
    postNo = db.Column(db.Integer)
    services = db.relationship('Service', backref='address', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'streetNo': self.streetNo,
            'street': self.street,
            'city': self.city,
            'post': self.post,
            'postNo': self.postNo,
            'services': [service.to_dict() for service in self.services]
        }
