# database/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base
from config import Config

engine = create_engine(Config.DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)
    print("[DB] Base de datos inicializada correctamente.")


def get_db():
    db = SessionLocal()
    try:
        return db
    except Exception as e:
        db.close()
        raise e