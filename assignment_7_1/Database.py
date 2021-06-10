from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, Sequence, String, Date, Float, BIGINT
from sqlalchemy.ext.declarative import declarative_base


def print_students(session, Students):
    students = session.query(Students).all()
    session.commit()
    if len(students) != 0:
        for stud in students:
            print(f"id: {stud.id}, name: {stud.name}, email: {stud.email}, year: {stud.year}")
    else:
        print("No students found")


def add_student(session, Students):
    new_stud = Students(id=len(session.query(Students).all()) + 1, name=str(input("Name: ")),
                        email=str(input("Email: ")),
                        year=int(input("Year: ")))
    session.add(new_stud)
    session.commit()
    stud_added = session.query(Students).get(len(session.query(Students).all()))
    print(f"Added student: id: {stud_added.id}, name: {stud_added.name}, email: {stud_added.email}, year: "
          f"{stud_added.year}")


def get_stud_by_id(session, Students):
    student = session.query(Students).get(int(input("id: ")))
    session.commit()
    if student is not None:
        print(f"id: {student.id}, name: {student.name}, email: {student.email}, year: "f"{student.year}")
    else:
        print("Student not found")


def edit_student(session, Students):
    student = session.query(Students).get(int(input('id: ')))
    if student is not None:
        student.name = str(input('name: '))
        student.email = str(input('email: '))
        student.year = int(input('year: '))
        session.commit()
        print("Student was edited successfully")
    else:
        session.commit()
        print("Student not found")


def remove_student(session, Students):
    student = session.query(Students).get(int(input('id: ')))
    if student is not None:
        session.delete(student)
        session.commit()
        print("Student was removed successfully")
    else:
        session.commit()
        print("Student not found")


def find_stud_ny_name(session, Students):
    Type_name = str(input("Type name: "))
    student = session.query(Students).filter(Students.name.like(f'{Type_name}')).all()
    student2 = session.query(Students).filter(Students.name == Type_name).all()
    if len(student2) != 0:
        for stud in student2:
            print(f"id: {stud.id}, name: {stud.name}, email: {stud.email}, year: {stud.year}")
    elif len(student) != 0:
        for stud in student:
            print(f"id: {stud.id}, name: {stud.name}, email: {stud.email}, year: {stud.year}")