import click
from sqlalchemy.exc import SQLAlchemyError

from app.commands import user
from app.database import sqlalchemy_engine, connection_string
from app.models.base import Base


@click.group()
def cli():
    pass


cli.add_command(user)


if __name__ == "__main":
    try:
        engine = sqlalchemy_engine(connection_string)
        engine.connect()
        Base.metadata.create_all(engine)
        cli()
    except SQLAlchemyError as e:
        print(f"Connection is failed: {e}")
