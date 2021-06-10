from Services.db import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)

    # Relationship
    car_rentals = db.relationship('Rental', backref='customer', lazy=True)

    def __repr__(self):
        return f"<id {self.id}>"
