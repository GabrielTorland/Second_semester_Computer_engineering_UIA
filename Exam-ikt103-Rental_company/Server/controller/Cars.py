from flask import *
from flask_restful import Resource
from werkzeug.exceptions import *
from Services.Marshmallow import cars_schema, car_schema
from Services.assignment_helpers import generate_cars
from model.Car import Car
from Services.db import db
from Services.Querys import Car_module, Rental_module


def generate_car():
    for i in range(1, 20):
        db.session.add(generate_cars(i))
    db.session.commit()


class CarResource(Resource, Car_module, Rental_module):

    def get(self, ID=None, Id=None, brand=None, Type=None, color=None):
        if Id:
            cars = self.get_car_by_id(Id)
            if not cars:
                raise BadRequest(f"Car with id {Id} doesn't exist")
            else:
                return car_schema.dump(cars)

        elif ID:
            cars = self.get_car_by_id(ID)
            if not cars:
                raise BadRequest(f"Car with id {ID} doesn't exist")
            else:
                total_price = {"tot_price": 0}
                for price in cars.car_rentals:
                    total_price['tot_price'] += price.price
                return total_price

        elif brand:
            cars = self.get_car_by_brand(brand)
            if len(cars) != 0:
                return cars_schema.dump(cars)
            else:
                raise BadRequest(f"Car with brand {brand} doesn't exist")

        elif Type:
            cars = self.get_car_by_type(Type)
            if len(cars) != 0:
                return cars_schema.dump(cars)
            else:
                raise BadRequest(f"Car with type {Type} doesn't exist")

        elif color:
            cars = self.get_car_by_color(color)
            if len(cars) != 0:
                return cars_schema.dump(cars)
            else:
                raise BadRequest(f"Car with color {color} doesn't exist")

        else:
            cars = self.get_all_cars()
            return cars_schema.dump(cars)

    def post(self):
        # Checking if car already exists.
        car = self.get_car_by_id(request.json['id'])
        if not car:
            new_car = Car(
                id=request.json['id'],
                type=request.json['type'],
                brand=request.json['brand'],
                color=request.json['color'],
                price_per_day=request.json['price_per_day']
            )
            self.add_car(new_car)
            return car_schema.dump(new_car)
        else:
            raise BadRequest(f"Car with id {request.json['id']} already exist")

    def put(self, Id):
        car = self.get_car_by_id(Id)
        if not car:
            raise BadRequest(f"Car with id {Id} doesn't exists.")
        else:
            if 'type' in request.json:
                car.type = request.json['type']
            if 'brand' in request.json:
                car.brand = request.json['brand']
            if 'color' in request.json:
                car.color = request.json['color']
            if 'price_per_day' in request.json:
                car.price_per_day = request.json['price_per_day']
            self.db.session.commit()
            return car_schema.dump(car)

    def delete(self, Id):
        car = self.get_car_by_id(Id)
        if not car:
            raise NotFound(f"Car with id {Id} doesn't exists.")

        elif len(self.get_rental_by_car_id(Id)) != 0:
            raise BadRequest(f"Rental with car_id {Id} exists")
        else:
            self.delete_car(car)
            return car_schema.dump(car)
