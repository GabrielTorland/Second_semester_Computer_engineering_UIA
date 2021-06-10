from flask_marshmallow import Marshmallow
from model.Car import Car
from model.Customer import Customer
from model.Rental import Rental
from .db import app

ma = Marshmallow(app)


# Creating new marshmallow schemas
class CarSchema(ma.Schema):
    class Meta:
        fields = ('id', 'type', 'brand', 'color', 'price_per_day')
        model = Car


car_schema = CarSchema()
cars_schema = CarSchema(many=True)


class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'fullname', 'email', 'phone')
        model = Customer


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)


class RentalSchema(ma.Schema):
    class Meta:
        fields = ('rental_id', 'start_time', 'end_time', 'price', 'car_id', 'customer_id')
        model = Rental


rental_schema = RentalSchema()
rentals_schema = RentalSchema(many=True)
