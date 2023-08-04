from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core import settings
from app.models.base import Base

postgresql_uri = f'postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}' \
                 f'@{settings.POSTGRES_SERVER}/{settings.POSTGRES_DB}'
engine = create_engine(postgresql_uri)
session = sessionmaker()
session.configure(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
