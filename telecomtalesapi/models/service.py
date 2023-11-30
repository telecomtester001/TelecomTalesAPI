from telecomtalesapi import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100))
    value = db.Column(db.Boolean)
    comment = db.Column(db.String(250))
   # address_id = db.Column(db.Integer, db.ForeignKey('address.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'service': self.service,
            'value': self.value,
            'comment': self.comment,
    #        'address_id': self.address_id
        }


# Associative table for Address and Service
address_service = db.Table('address_service',
    db.Column('address_id', db.Integer, db.ForeignKey('address.id'), primary_key=True),
    db.Column('service_id', db.Integer, db.ForeignKey('service.id'), primary_key=True)
)