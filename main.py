from sqlalchemy.exc import SQLAlchemyError

from app.commands import hello
from app.database import sqlalchemy_engine, connection_string
from app.models.base import Base
from app.models.book import Book

if __name__ == "__main__":
    try:
        print(connection_string)
        engine = sqlalchemy_engine(connection_string)
        engine.connect()
        Base.metadata.create_all(engine)
        hello()

    except SQLAlchemyError as e:
        print(f"Connection is failed: {e}")
