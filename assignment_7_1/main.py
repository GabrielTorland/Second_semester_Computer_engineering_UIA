from sqlalchemy.orm import sessionmaker
from sqlalchemy import Text
from Database import print_students, add_student, get_stud_by_id, edit_student, remove_student, find_stud_ny_name
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///school.sqlite", echo=True)
Base = declarative_base()


class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    email = Column(Text)
    year = Column(Integer)


def main():
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    while True:
        c = str(input("Option [1-7]: "))
        if c == "1":
            print_students(session, Students)
        elif c == "2":
            get_stud_by_id(session, Students)
        elif c == "3":
            add_student(session, Students)
        elif c == "4":
            edit_student(session, Students)
        elif c == "5":
            remove_student(session, Students)
        elif c == '6':
            find_stud_ny_name(session, Students)
        elif c == '7':
            break
        elif c == 'd':
            deleted = session.query(Students).delete()
            print(deleted)
            session.commit()


if __name__ == "__main__":
    main()
