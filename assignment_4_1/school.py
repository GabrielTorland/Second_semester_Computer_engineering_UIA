
class Student:
    def __init__(self, id, name, age, attendance):
        self.id = id
        self.name = name
        self.age = age
        self.attendance = attendance

    def ages(self):
        oldest_student = 0
        youngest_student = 100
        for obj in self:
            if obj.age <= youngest_student:
                youngest_student = obj.age
                young = obj.name
            if obj.age >= oldest_student:
                oldest_student = obj.age
                old = obj.name
        print(f"Youngest: {young}")
        print(f"Oldest: {old}")

    def average_age(self):
        temp = 0
        for obj in self:
            temp += obj.age
        print(f"Average age: {int(temp/len(self))}")

    def Bad_stud(self):
        for obj in self:
            if obj.attendance < 30:
                print(f"Bad student: {obj.name}")
