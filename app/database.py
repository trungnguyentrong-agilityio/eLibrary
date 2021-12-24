from sqlalchemy import create_engine


def build_postgres_connection_string(user: str, pwd: str, database: str, port: int, host: str = "localhost") -> str:
    return f"postgresql://{user}:{pwd}@{host}:{str(port)}/{database}"


def sqlalchemy_engine(connection_string: str):
    return create_engine(connection_string, pool_recycle=3600)
