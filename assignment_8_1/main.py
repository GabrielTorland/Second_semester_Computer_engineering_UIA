from Functions import *
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

# Shows the sql code that is happening in the background.
engine = create_engine("sqlite:///school.sqlite")
Base = declarative_base()


class Students_courses_table(Base):
    __tablename__ = 'students_courses'

    student_id = Column(Integer, ForeignKey("students.id"), primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"), primary_key=True)

    studs_has_class = relationship("Students", back_populates='studs')
    class_has_studs = relationship("Courses", back_populates='study')


class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    email = Column(Text)
    year = Column(Integer)

    studs = relationship("Students_courses_table", back_populates='studs_has_class')


class Courses(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    max_students = Column(Integer)

    study = relationship("Students_courses_table", back_populates='class_has_studs')
    tests = relationship("Tests", back_populates='course')


class Tests(Base):
    __tablename__ = 'tests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    date_time = Column(Text)
    course_id = Column(Integer, ForeignKey('courses.id'))

    course = relationship("Courses", back_populates='tests')


def main():
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    while True:
        print("1. Add student\n"
              "2. Add course\n"
              "3. Add test\n"
              "4. Add student to course\n"
              "5. List courses by student\n"
              "6. List tests by course\n"
              "7. Exit")
        c = str(input("Option [1-7]: "))
        if c == "1":
            add_student(session, Students)
        elif c == "2":
            add_course(session, Courses)
        elif c == "3":
            add_test(session, Tests)
        elif c == "4":
            add_stud_to_course(session, Students, Courses, Students_courses_table)
        elif c == "5":
            print_courses(session, Students_courses_table, Courses)
        elif c == '6':
            print_tests(session, Tests)
        elif c == '7':
            break
        elif c == 'd':
            session.query(Students).delete()
            session.query(Courses).delete()
            session.query(Tests).delete()
            session.commit()
        else:
            break


if __name__ == '__main__':
    main()
