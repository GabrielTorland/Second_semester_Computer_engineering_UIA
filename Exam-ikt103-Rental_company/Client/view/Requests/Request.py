import requests

Base_url = "http://127.0.0.1:5000"


def car(get=False, post=False, delete=False, put=False, ID=None, tot_price_ID=None, brand=None, Type=None, color=None,
        json=None):
    if get and tot_price_ID:
        return requests.get(f"{Base_url}/cars/total_price/{tot_price_ID}").json()
    elif get and ID:
        return requests.get(f"{Base_url}/cars/{ID}").json()
    elif get and brand:
        return requests.get(f"{Base_url}/cars/brand/{brand}").json()
    elif get and Type:
        return requests.get(f"{Base_url}/cars/type/{Type}").json()
    elif get and color:
        return requests.get(f"{Base_url}/cars/color/{color}").json()
    elif post and json:
        return requests.post(f"{Base_url}/cars", json=json).json()
    elif delete and ID:
        return requests.delete(f"{Base_url}/cars/{ID}").json()
    elif put and json:
        return requests.put(f"{Base_url}/cars/{json['id']}", json=json).json()
    else:
        return requests.get(f"{Base_url}/cars").json()


def customer(get=False, post=False, delete=False, put=False, ID=None, fullname=None, email=None, phone=None, json=None):
    if get and ID:
        return requests.get(f"{Base_url}/customers/{ID}").json()
    elif get and email:
        return requests.get(f"{Base_url}/customers/email/{email}").json()
    elif get and fullname:
        return requests.get(f"{Base_url}/customers/fullname/{fullname}").json()
    elif get and phone:
        return requests.get(f"{Base_url}/customers/phone/{phone}").json()
    elif post and json:
        return requests.post(f"{Base_url}/customers", json=json).json()
    elif put and json:
        return requests.put(f"{Base_url}/customers/{json['id']}", json=json).json()
    elif delete and ID:
        return requests.delete(f"{Base_url}/customers/{ID}").json()
    else:
        return requests.get(f"{Base_url}/customers").json()


def rentals(get=False, post=False, delete=False, put=False, rental_id=None, car_id=None, customer_id=None, json=None):
    if get and rental_id:
        return requests.get(f"{Base_url}/rentals/{rental_id}").json()
    elif get and car_id:
        return requests.get(f"{Base_url}/rentals/car/{car_id}").json()
    elif get and customer_id:
        return requests.get(f"{Base_url}/rentals/customer/{customer_id}").json()
    elif post and json:
        return requests.post(f"{Base_url}/rentals", json=json).json()
    elif put and json:
        return requests.put(f"{Base_url}/rentals/{json['rental_id']}", json=json).json()
    elif delete and rental_id:
        return requests.delete(f"{Base_url}/rentals/{rental_id}").json()
    else:
        return requests.get(f"{Base_url}/rentals").json()
