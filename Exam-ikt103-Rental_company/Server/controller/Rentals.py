from flask import *
import datetime
from datetime import date
from flask_restful import Resource
from werkzeug.exceptions import *
from Services.Marshmallow import rental_schema, rentals_schema
from model.Rental import Rental
from Services.db import db
from Services.assignment_helpers import generate_rentals
from Services.Querys import Rental_module, Car_module, Customer_module


def generate_rental():
    for i in range(10):
        db.session.add(generate_rentals(i))
    db.session.commit()


class RentalResource(Resource, Rental_module, Car_module, Customer_module):
    # Defining get.
    # Setting parameters to None, so i dont need to send them every time.
    def get(self, car_id=None, customer_id=None, rental_id=None):
        # Get request with car_id.
        if car_id:
            rental = self.get_rental_by_car_id(car_id)
            if len(rental) != 0:
                return rentals_schema.dump(rental)
            else:
                raise BadRequest(f"Rental with car_id {car_id} doesn't exist")

        # Get request with customer_id.
        elif customer_id:
            rental = self.get_rental_by_customer_id(customer_id)
            if len(rental) != 0:
                return rentals_schema.dump(rental)
            else:
                raise BadRequest(f"Rental with customer_id {customer_id} doesn't exist")

        # Get request with rental_id.
        elif rental_id:
            rental = self.get_rental_by_rental_id(rental_id)
            if rental:
                return rental_schema.dump(rental)
            else:
                raise BadRequest(f"Rental with rental_id {rental_id} doesn't exist")

        # Get request all from Rental.
        else:
            rentals = self.get_all_rentals()
            return rentals_schema.dump(rentals)

    # Defining post.
    def post(self):
        # Searching for a specific car and customer, returning a list.
        state = self.get_car_by_id(request.json['car_id'])
        state2 = self.get_customer_by_id(request.json['customer_id'])
        # Checking if both these list doesnt have length 0, because they need to exist to use them.
        if state and state2:
            # Changing str to datetime object.
            t_0 = datetime.datetime.strptime(request.json['start_time'], "%Y-%m-%d %H:%M:%S")
            t_1 = datetime.datetime.strptime(request.json['end_time'], "%Y-%m-%d %H:%M:%S")

            if self.check_date(t_0, t_1, request.json['car_id']):
                raise NotAcceptable(f"Car with id {request.json['car_id']} is occupied at this date")
            else:
                new_rental = Rental(
                    start_time=t_0,
                    end_time=t_1,
                    price=(t_1-t_0).days * state.price_per_day,
                    car_id=request.json['car_id'],
                )
                state2.car_rentals.append(new_rental)
                self.commiter()
                return rental_schema.dump(new_rental)
        else:
            if not state and not state2:
                raise BadRequest("Missing car and customer.")
            elif not state:
                raise BadRequest("Missing car.")
            else:
                raise BadRequest("Missing customer ")

    # Defining put.
    def put(self, rental_id):
        # Retrieving data from rental_id
        rental = self.get_rental_by_rental_id(rental_id)

        if rental:
            # Checking if the json data contains car_id.
            if 'car_id' in request.json:
                # Checking if the car exists in the Car table.
                if self.get_car_by_id(request.json['car_id']) is not None:
                    rental.car_id = request.json['car_id']
                else:
                    raise NotFound('Car doesnt exist')

            # Checking if the json data contains start_time.
            if 'start_time' and 'end_time' in request.json:

                # Changing str to datetime object.
                # You have to change both start_time and end_time in one put request.
                t_0 = datetime.datetime.strptime(request.json['start_time'], "%Y-%m-%d %H:%M:%S")
                t_1 = datetime.datetime.strptime(request.json['end_time'], "%Y-%m-%d %H:%M:%S")

                # Checking if start_time is occupied for this specific car.
                if self.check_date_put(t_0, t_1, rental):
                    raise NotFound(f"Car with id {rental.car_id} is occupied at this date")
                else:
                    rental.start_time = t_0
                    rental.end_time = t_1
                    rental.price = (t_1-t_0).days * int(self.get_car_by_id(rental.car_id).price_per_day)

            # Repeating the same if statements for customer_id as car_id.
            if 'customer_id' in request.json:
                if self.get_customer_by_id(request.json['customer_id']) is not None:
                    rental.customer_id = request.json['customer_id']
                else:
                    raise NotFound('Customer doesnt exist')

            self.commiter()
            return rental_schema.dump(rental)
        else:
            raise BadRequest(f"Rental with rental_id {rental_id} doesn't exist")

    # Defining delete.
    def delete(self, rental_id):
        rental = self.get_rental_by_rental_id(rental_id)
        if rental:
            self.delete_rental(rental)
            return rental_schema.dump(rental)
        else:
            raise BadRequest(f"Rental with rental_id {rental_id} doesn't exist")
