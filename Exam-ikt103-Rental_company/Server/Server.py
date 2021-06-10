from flask_restful import Api
from controller.Rentals import generate_rental, RentalResource
from controller.Cars import generate_car, CarResource
from controller.Customers import generate_customer, CustomerResource
from Services.db import *


api = Api(app)

db.drop_all()
db.create_all()


# Generating some data to start with.
generate_customer()
generate_car()
generate_rental()

api.add_resource(CarResource, '/cars',
                 '/cars/<Id>',
                 '/cars/total_price/<ID>',
                 '/cars/brand/<brand>',
                 '/cars/type/<Type>',
                 '/cars/color/<color>')

api.add_resource(RentalResource, '/rentals',
                 '/rentals/car/<car_id>',
                 '/rentals/customer/<customer_id>',
                 '/rentals/<rental_id>')

api.add_resource(CustomerResource, '/customers',
                 '/customers/<Id>',
                 '/customers/fullname/<fullname>',
                 '/customers/email/<email>',
                 '/customers/phone/<phone>')

if __name__ == '__main__':
    app.run(debug=True)
