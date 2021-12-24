from sqlalchemy.exc import SQLAlchemyError

from app.commands import hello
from app.database import build_postgres_connection_string, sqlalchemy_engine
from app.config import Config

config = Config()

if __name__ == "__main__":
    connection_string = build_postgres_connection_string(
        user=config.POSTGRES_USER,
        database=config.POSTGRES_DB,
        pwd=config.POSTGRES_PASSWORD,
        host=config.POSTGRES_HOST,
        port=config.POSTGRES_PORT,
    )
    try:
        print(connection_string)
        engine = sqlalchemy_engine(connection_string)
        engine.connect()
        hello()
    except SQLAlchemyError as e:
        print(f"Connection is failed: {e}")
