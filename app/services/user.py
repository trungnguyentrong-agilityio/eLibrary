from app.database import sqlalchemy_session
from app.models import Book
from app.models.book import BookStatus
from app.models.user import User
from app.database import connection_string
import click

from app.serializers import UserSchema
from app.serializers.user import UserBorrowingSchema

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


def borrow_book(user_id: int, book_id: int):
    try:
        user = session.get(User, {"id": user_id})
        book = session.get(Book, {"id": book_id})

        if not user:
            click.echo("User not Found")
            return

        if not book:
            click.echo("Book not Found")
            return

        if book.status == BookStatus.unavailable:
            click.echo("This book isn't available")
            return

        book.user_id = user.id
        book.status = BookStatus.unavailable
        session.commit()
    except:
        session.rollback()
        raise


def return_book(user_id: int, book_id: int):
    try:
        user = session.get(User, {"id": user_id})
        book = session.get(Book, {"id": book_id})

        if not user:
            click.echo("User not Found")
            return

        if not book:
            click.echo("Book not Found")
            return

        book.user_id = None
        book.status = BookStatus.available
        session.commit()
    except:
        session.rollback()
        raise


def borrowing_list(user_id: int):
    try:
        user = session.get(User, {"id": user_id})

        if not user:
            click.echo("User not Found")
            return

        return UserBorrowingSchema().dumps(user)
    except:
        session.rollback()
        raise