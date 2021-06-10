import json
from school import Student

def print_hi(name):
    students = []
    with open('students.json') as jason_file:
        data = json.load(jason_file)
        for i in range(len(data)):
            students.append(Student(int(data[i]['id']), data[i]['name'], int(data[i]['age']), int(data[i]['attendance'])))
    Student.ages(students)
    Student.average_age(students)
    Student.Bad_stud(students)

if __name__ == '__main__':
    print_hi('PyCharm')
