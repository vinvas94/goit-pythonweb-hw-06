from faker import Faker
import random
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Group, Student, Teacher, Subject, Grade

fake = Faker()
engine = create_engine("postgresql://postgres:claveSegura123@localhost:5432/postgres")
Session = sessionmaker(bind=engine)
session = Session()

def seed_data():
    # Groups
    groups = [Group(name=f"Group {i}") for i in range(1, 4)]
    session.add_all(groups)

    # Teachers
    teachers = [Teacher(name=fake.name()) for _ in range(4)]
    session.add_all(teachers)

    # Subjects
    subjects = [Subject(name=fake.word().capitalize(), teacher=random.choice(teachers)) for _ in range(6)]
    session.add_all(subjects)

    # Students
    students = []
    for _ in range(50):
        group = random.choice(groups)
        student = Student(name=fake.name(), group=group)
        students.append(student)
    session.add_all(students)

    # Grades
    for student in students:
        for subject in subjects:
            for _ in range(random.randint(3, 6)):
                grade = Grade(
                    student=student,
                    subject=subject,
                    grade=round(random.uniform(60, 100), 2),
                    date_received=fake.date_between(start_date='-1y', end_date='today')
                )
                session.add(grade)

    session.commit()

if __name__ == "__main__":
    seed_data()
