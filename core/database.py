from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase

DATABASE_URL="sqlite:///expenses.db"

engine=create_engine(DATABASE_URL,connect_args={"check_same_thread":False})

LocalSession=sessionmaker(bind=engine,autocommit=False,autoflush=False)

class Base(DeclarativeBase):
    pass

def get_db():
    db=LocalSession()
    try:
        yield db
    finally:
        db.close()