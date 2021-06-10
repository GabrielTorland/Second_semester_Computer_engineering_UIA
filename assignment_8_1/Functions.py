from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Text, Column, Integer, String, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base



def add_student(session, Students):
    new_stud = Students(name=str(input("Name: ")), email=str(input("Email: ")), year=int(input("Year: ")))
    session.add(new_stud)
    session.commit()
    print(f"Added student with id {new_stud.id}")


def add_course(session, Courses):
    new_course = Courses(name=str(input("name: ")), max_students=int(input("Max students: "
                                                                           "")))
    session.add(new_course)
    session.commit()
    print(f"Added course with id {new_course.id}")


def add_test(session, Tests):
    new_test = Tests(course_id=int(input("CId: ")), name=str(input("name: ")), date_time=str(input("Date: ")))
    session.add(new_test)
    session.commit()
    print(f"Added test with id {new_test.id}")


def add_stud_to_course(session, Students, Course, students_courses_table):
    stud = session.query(Students).get(int(input('SId: ')))
    if stud is None:
        print(f"Student not found")
        return
    course = session.query(Course).get(int(input("CId: ")))
    if course is None:
        print("Course not found")
        return

    elif course and stud is not None:
        session.add(students_courses_table(student_id=stud.id, course_id=course.id))
        session.commit()
        print(f"Added student to course id {course.id}")


def print_courses(session, student_courses_table, Courses):
    studs_course = session.query(student_courses_table).filter(student_courses_table.student_id.like(int(input("Id: ")))
                                                               ).all()
    if len(studs_course) != 0:
        print(f"Courses for student {studs_course[0].student_id}: ", end="")
        studs_course.sort(key=lambda x: x.course_id)
        print(", ".join(session.query(Courses).get(course.course_id).name for course in studs_course))
    else:
        print("Student not found")


def print_tests(session, Tests):
    tests = session.query(Tests).filter(Tests.course_id.like(int(input("Id: ")))).all()
    if len(tests) != 0:
        tests.sort(key=lambda x: x.id)
        print(f"Tests for course {tests[0].course_id}: ", end="")
        print(", ".join(session.query(Tests).get(test.id).name for test in tests))
    else:
        print("Course not found")
