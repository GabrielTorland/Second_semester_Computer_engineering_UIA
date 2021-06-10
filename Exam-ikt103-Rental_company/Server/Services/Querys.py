from model.Car import Car
from model.Customer import Customer
from model.Rental import Rental
from .db import db


class database:
    def __init__(self):
        self.db = db


class Customer_module(database):
    def get_all_customers(self):
        return self.db.session.query(Customer).all()

    def get_customer_by_id(self, Id):
        customer = self.db.session.query(Customer).get(Id)
        return customer

    def get_customer_by_fullname(self, fullname):
        return self.db.session.query(Customer).filter(Customer.fullname.ilike(f"%{fullname}%")).all()

    def get_customer_by_email(self, email):
        return self.db.session.query(Customer).filter(Customer.email.ilike(f"%{email}%")).all()

    def get_customer_by_phone(self, phone):
        return self.db.session.query(Customer).filter(Customer.phone.ilike(f"%{phone}%")).all()

    def add_customer(self, new_customer):
        self.db.session.add(new_customer)
        self.db.session.commit()

    def delete_customer(self, customer):
        self.db.session.delete(customer)
        self.db.session.commit()


class Car_module(database):
    def get_all_cars(self):
        return self.db.session.query(Car).all()

    def get_car_by_id(self, Id):
        car = self.db.session.query(Car).get(Id)
        return car

    def get_car_by_brand(self, brand):
        return self.db.session.query(Car).filter(Car.brand.ilike(f"%{brand}%")).all()

    def get_car_by_type(self, Type):
        return self.db.session.query(Car).filter(Car.type.ilike(f"%{Type}%")).all()

    def get_car_by_color(self, color):
        return self.db.session.query(Car).filter(Car.color.ilike(f"%{color}%")).all()

    def add_car(self, new_car):
        self.db.session.add(new_car)
        self.db.session.commit()

    def delete_car(self, car):
        self.db.session.delete(car)
        self.db.session.commit()


class Rental_module(database):
    def get_all_rentals(self):
        return self.db.session.query(Rental).all()

    def get_rental_by_car_id(self, car_id):
        rental = self.db.session.query(Rental).filter(Rental.car_id.like(car_id)).all()
        return rental

    def get_rental_by_customer_id(self, customer_id):
        rental = self.db.session.query(Rental).filter(Rental.customer_id.like(customer_id)).all()
        return rental

    def get_rental_by_rental_id(self, rental_id):
        return self.db.session.query(Rental).get(rental_id)

    def get_car_by_car_ID(self, car_id):
        return self.db.session.query(Car).filter(car_id == Car.id).scalar()

    def get_customer_by_customer_ID(self, customer_id):
        return self.db.session.query(Customer).filter(customer_id == Customer.id).scalar()

    def check_date(self, t_0, t_1, car_id):
        return self.db.session.query(Rental).filter(Rental.car_id.like(car_id)). \
            filter(db.between(Rental.start_time, t_0, t_1) |
                   (db.between(Rental.end_time, t_0, t_1)) |
                   (db.between(t_0, Rental.start_time, Rental.end_time)) |
                   (db.between(t_1, Rental.start_time, Rental.end_time))).all()

    def check_date_put(self, t_0, t_1, rental):
        return self.db.session.query(Rental).filter(Rental.rental_id != rental.rental_id) \
            .filter(Rental.car_id.like(rental.car_id)). \
            filter(db.between(Rental.start_time, t_0, t_1) |
                   (db.between(Rental.end_time, t_0, t_1)) |
                   (db.between(t_0, Rental.start_time, Rental.end_time)) |
                   (db.between(t_1, Rental.start_time, Rental.end_time))).all()

    def commiter(self):
        self.db.session.commit()

    def delete_rental(self, rental):
        self.db.session.delete(rental)
        self.db.session.commit()
