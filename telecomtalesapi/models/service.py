from telecomtalesapi import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100))
    value = db.Column(db.Boolean)
    comment = db.Column(db.String(250))
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'service': self.service,
            'value': self.value,
            'comment': self.comment,
            'address_id': self.address_id
        }
