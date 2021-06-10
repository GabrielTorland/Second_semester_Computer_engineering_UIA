import random
from faker import Faker
from model.Car import Car
from model.Customer import Customer
from model.Rental import Rental
from .db import db
import datetime

faker = Faker('no_NO')


def list_cars():
    data = []
    with open("Services/car_list.txt", 'r') as cars:
        for line in cars:
            current_place = line[3:-3]
            data.append(current_place)
    return data


def car_types():
    types = []
    with open("Services/car_types.txt", 'r') as Type:
        for t in Type:
            types.append(f"{t[:-1]}")
    return types


def generate_cars(ID):
    return Car(id=1000 + ID, type=car_types()[ID], brand=list_cars()[ID],
               color=faker.color_name(), price_per_day=random.randint(50, 1000))


def generate_customers():
    name = faker.name()
    return Customer(fullname=name, email='.'.join(name.lower().split()) + '@' + faker.free_email_domain(),
                    phone=faker.phone_number())


def generate_rentals(ID):
    cars = db.session.query(Car).all()
    t_0 = datetime.datetime(2021 + ID, 2, 1, 12, 0, 0, 0)
    t_1 = datetime.datetime(2021 + ID, 2, 2, 12, 0, 0, 0)
    customers = db.session.query(Customer).all()
    return Rental(start_time=t_0,
                  end_time=t_1, price=(t_1.day - t_0.day) * cars[ID].price_per_day, car_id=cars[ID].id,
                  customer_id=customers[ID].id)
