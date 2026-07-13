from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://IT215-FastAPI:du123456789%40@127.0.0.1:3306/class_section_db"

engoige = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engoige,
    autoflush=False,
    autocommit=False
)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
