from flask import *
from flask_restful import Resource
from werkzeug.exceptions import *
from Services.Marshmallow import customer_schema, customers_schema
from model.Customer import Customer
from Services.db import db
from Services.Querys import Customer_module, Rental_module
from Services.assignment_helpers import generate_customers


def generate_customer():
    for i in range(1, 2000):
        db.session.add(generate_customers())
    db.session.commit()


class CustomerResource(Resource, Customer_module, Rental_module):
    def get(self, Id=None, fullname=None, email=None, phone=None):
        if Id:
            customer = self.get_customer_by_id(Id)
            if customer:
                return customer_schema.dump(customer)
            else:
                raise BadRequest(f"Customer with id {Id} doesn't exist")

        elif fullname:
            customer = self.get_customer_by_fullname(fullname)
            if len(customer) != 0:
                return customers_schema.dump(customer)
            else:
                raise BadRequest(f"Customer with fullname {fullname} doesn't exist")

        elif email:
            customer = self.get_customer_by_email(email)
            if len(customer) != 0:
                return customers_schema.dump(customer)
            else:
                raise BadRequest(f"Customer with email {email} doesn't exist")

        elif phone:
            customer = self.get_customer_by_phone(phone)
            if len(customer) != 0:
                return customers_schema.dump(customer)
            else:
                raise BadRequest(f"Customer with phone number {phone} doesn't exist")

        else:
            customer = self.get_all_customers()
            return customers_schema.dump(customer)

    def post(self):
        new_customer = Customer(
            fullname=request.json['fullname'],
            email=request.json['email'],
            phone=request.json['phone']
        )
        self.add_customer(new_customer)
        return customer_schema.dump(new_customer)

    def put(self, Id):
        customer = self.get_customer_by_id(Id)
        if customer:
            if 'fullname' in request.json:
                customer.fullname = request.json['fullname']
            if 'email' in request.json:
                customer.email = request.json['email']
            if 'phone' in request.json:
                customer.phone = request.json['phone']
            db.session.commit()
            return customer_schema.dump(customer)
        else:
            raise BadRequest(f"Customer with id {Id} doesn't exist")

    def delete(self, Id):
        customer = self.get_customer_by_id(Id)
        if not customer:
            raise BadRequest(f"Customer with id {Id} doesn't exist")
        elif len(self.get_rental_by_customer_id(Id)) != 0:
            raise BadRequest(f"Rental with customer_id {Id} exists")
        else:
            self.delete_customer(customer)
            return customer_schema.dump(customer)

