from sqlalchemy import func, desc
from app.models import Student, Subject, Teacher, Grade, Group
from app.db import with_session


@with_session
def select_1(session):
    return session.query(
        Student.name,
        func.avg(Grade.grade).label("avg_grade")
    ).join(Grade).group_by(Student.id).order_by(desc("avg_grade")).limit(5).all()


@with_session
def select_2(session, subject_id: int):
    return session.query(
        Student.name,
        func.avg(Grade.grade).label("avg_grade")
    ).join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id).order_by(desc("avg_grade")).first()


@with_session
def select_3(session, subject_id: int):
    return session.query(
        Group.name,
        func.avg(Grade.grade).label("avg_grade")
    ).select_from(Group) \
     .join(Student, Student.group_id == Group.id) \
     .join(Grade, Grade.student_id == Student.id) \
     .filter(Grade.subject_id == subject_id) \
     .group_by(Group.id).all()


@with_session
def select_4(session):
    return session.query(func.avg(Grade.grade)).scalar()


@with_session
def select_5(session, teacher_id: int):
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()


@with_session
def select_6(session, group_id: int):
    return session.query(Student.name).filter(Student.group_id == group_id).all()


@with_session
def select_7(session, group_id: int, subject_id: int):
    return session.query(
        Student.name,
        Grade.grade
    ).join(Grade).filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()


@with_session
def select_8(session, teacher_id: int):
    return session.query(
        func.avg(Grade.grade)
    ).join(Subject).filter(Subject.teacher_id == teacher_id).scalar()


@with_session
def select_9(session, student_id: int):
    return session.query(
        Subject.name
    ).join(Grade).filter(Grade.student_id == student_id).distinct().all()


@with_session
def select_10(session, student_id: int, teacher_id: int):
    return session.query(
        Subject.name
    ).join(Grade).filter(
        Grade.student_id == student_id,
        Subject.teacher_id == teacher_id
    ).distinct().all()
