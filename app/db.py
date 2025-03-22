from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from functools import wraps

DB_URL = "postgresql://postgres:claveSegura123@localhost:5432/postgres"

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

# Декоратор для автоматичного керування сесією
def with_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session = Session()
        try:
            result = func(session, *args, **kwargs)
        finally:
            session.close()
        return result
    return wrapper
