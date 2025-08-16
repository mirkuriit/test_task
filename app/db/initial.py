from sqlalchemy import create_engine
from app.config import config
from app.db.tables import Base


engine = create_engine(config.DATABASE_URL_SYNC, echo=True)


def create_db():
    Base.metadata.create_all(bind=engine)


def drop_db():
    Base.metadata.drop_all(bind=engine)
