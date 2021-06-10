from Services.db import db


class Rental(db.Model):
    rental_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_time = db.Column(db.DATETIME, nullable=False)
    end_time = db.Column(db.DATETIME, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    def __repr__(self):
        return f"<car_id {self.car_id}, customer_id {self.customer_id}>"

