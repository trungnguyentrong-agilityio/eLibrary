from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app.config import Config

config = Config()

def build_postgres_connection_string(user: str, pwd: str, database: str, port: int, host: str = "localhost") -> str:
    return f"postgresql://{user}:{pwd}@{host}:{str(port)}/{database}"


def sqlalchemy_engine(connection_string: str):
    return create_engine(connection_string, pool_recycle=3600)

def sqlalchemy_session(connection_string):
    return scoped_session(
        sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=sqlalchemy_engine(connection_string),
        )
    )

connection_string = build_postgres_connection_string(
        user=config.POSTGRES_USER,
        database=config.POSTGRES_DB,
        pwd=config.POSTGRES_PASSWORD,
        host=config.POSTGRES_HOST,
        port=config.POSTGRES_PORT,
    )
