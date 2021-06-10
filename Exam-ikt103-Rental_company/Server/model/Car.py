from Services.db import db


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    brand = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)
    price_per_day = db.Column(db.Integer, nullable=False)

    # Relationship
    car_rentals = db.relationship('Rental', backref='car', lazy=True)

    def __repr__(self):
        return f"<id {self.id}>"
