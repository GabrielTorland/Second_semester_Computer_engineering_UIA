import requests

base_url = 'http://0.0.0.0:5000'


def menu():
    print(f"[1].Read all students")
    print(f"[2].Get student by id")
    print(f"[3].Add student")
    print(f"[4].Edit student")
    print(f"[5].Remove student")
    print(f"[6].Exit")


def student():
    response = requests.get(f"{base_url}/students").json()
    for obj in response:
        print(f"id: {obj['id']}, name: {obj['name']}, email: {obj['email']}, year: {obj['year']} ")


def your_info():
    state = True
    stud_id = {"id": int(input("Type your student id: "))}
    response = requests.get(f"{base_url}/students").json()
    for obj in response:
        if obj['id'] == stud_id['id']:
            print(f"id: {obj['id']}, name: {obj['name']}, email: {obj['email']}, year: {obj['year']} ")
            state = False
    if state:
        print("Student not found")


def add_students():
    response = requests.get(f"{base_url}/students").json()
    temp_dict = {
        "id": len(response) + 1,
        "name": str(input("Name: ")),
        "email": str(input("Email: ")),
        "year": int(input("Year: "))
    }
    requests.post(f"{base_url}/students", json=temp_dict)

    print(f"Added student: id: {temp_dict['id']}, name: {temp_dict['name']}, email: "
          f"{temp_dict['email']}, year: {temp_dict['year']}")


def edit_student():
    ID = int(input("Id: "))
    temp_dict = {
        "id": ID,
        "name": str(input("Name: ")),
        "email": str(input("Email: ")),
        "year": int(input("Year: "))
    }
    if requests.put(f"{base_url}/students/{ID}", json=temp_dict).status_code < 400:
        print("Student was edited successfully")

    else:
        print("Student not found")


def delete_student():
    id1 = input("Id: ")
    if requests.delete(f"{base_url}/students/{id1}").status_code == 204:
        print("Student was removed successfully")
    else:
        print("Student not found")
