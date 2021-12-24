from os import environ

from dotenv import load_dotenv

load_dotenv()


class Config:
    POSTGRES_USER = environ.get("POSTGRES_USER", "admin")
    POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD", "admin")
    POSTGRES_PORT = int(environ.get("POSTGRES_PORT", 5432))
    POSTGRES_DB = environ.get("POSTGRES_DB", "db")
    POSTGRES_HOST = environ.get("POSTGRES_HOST", "localhost")
