#import sqlalchmey declarative base, sessionmaker from orm
#import column, integer, string, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import Column, String, Integer, create_engine

#intialize declarative base
Base = declarative_base()
#Create a class for a table and inherit from base
#Create Student class and table
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(Integer)

#Create a teacher class and table
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    subject = Column(String)
    email = Column(String)

#Create a schedule class and table
class Schedule(Base):
    __tablename__ = 'schedules'

    id = Column(Integer, primary_key=True)


#Run code in this file by using if __name__ == "__main__":
if __name__ == '__main__':
    #create the engine
    engine = create_engine('sqlite:///school.db')
    
    #Drop all the tables
    # Teacher.__table__.drop(engine)
    # Student.__table__.drop(engine)
    # Schedule.__table__.drop(engine)
    #Set the metadata Base.metadata.create_all(engine)
    Base.metadata.create_all(engine)
    #Create a session from the engine, allowing us to work with the data
    # Session = sessionmaker(bind=engine)
    # session = Session()

    #Change the session to with Session(engine) as session:
    with Session(engine) as session: 

        #create multiple students
        stephen = Student(name = "Stephen",code = 1)
        josh = Student(name="Josh", code = 2)
        #add students to the session and commit
        session.add_all([stephen, josh])
        session.commit()
        #accept user input and ask to delete a student, 
        #if user input is "Yes" delete the student from the session and commit
        user_input = input("Choose a student by code: ")
        student = session.query(Student).filter(Student.code == user_input).first()

        user_input2 = input(f"Delete {student.name}? ")

        if user_input2 == "Yes":
            print("Deleting Student")
            session.delete(student)
            session.commit()










