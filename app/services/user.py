from app.database import sqlalchemy_session
from app.models.user import User
from app.database import connection_string
import click

from app.serializers import UserSchema

session = sqlalchemy_session(connection_string)


def create(firstname: str, lastname: str):
    try:
        user = User()
        user.firstname = firstname
        user.lastname = lastname

        session.add(user)
        session.commit()
        return UserSchema().dumps(user)
    except:
        session.rollback()
        raise


def get(identity: int):
    try:
        user = session.get(User, {"id": identity})

        if not user:
            click.echo("Not Found")
            return

        return UserSchema().dumps(user)
    except:
        session.rollback()
        raise


def getAll():
    try:
        users = session.query(User).all()

        return UserSchema().dumps(users, many=True)
    except:
        session.rollback()
        raise


def update(identity: int, firstname: str, lastname: str):
    try:
        user = session.get(User, {"id": identity})
        if not user:
            click.echo("Not Found")
            return

        user.firstname = firstname
        user.lastname = lastname

        session.commit()
        return UserSchema().dumps(user)
    except:
        session.rollback()
        raise


def delete(identity: int):
    try:
        user = session.get(User, {"id": identity})

        if not user:
            click.echo("Not Found")
            return

        session.delete(user)
        session.commit()
    except:
        session.rollback()
        raise
