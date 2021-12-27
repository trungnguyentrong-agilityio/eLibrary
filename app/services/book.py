import click
from app.database import sqlalchemy_session
from app.models.book import Book
from app.database import connection_string
from app.serializers import BookSchema

session = sqlalchemy_session(connection_string)

def get_all():
    try:
        book = session.query(Book).all()

        return BookSchema().dumps(book, many=True)
    except:
        session.rollback()
        raise

def get_one(identity: int):
    try:
        book = session.get(Book, {"id": identity})

        if not book:
            click.echo("Not Found")
            return

        return BookSchema().dumps(book)
    except:
        session.rollback()
        raise

def create(profile_id: int):
    try:
        book = Book()
        book.profile_id = profile_id

        session.add(book)
        session.commit()

        return BookSchema().dumps(book)
    except:
        session.rollback()
        raise

def update(identity: int, status: str, due_date: str, profile_id: int, user_id: int):
    try:
        book = session.get(Book, {"id": identity})

        if not book:
            click.echo("Not Found")
            return

        book.status = status
        book.due_date = due_date
        book.profile_id = profile_id
        book.user_id = user_id
        session.commit()

        return BookSchema().dumps(book)
    except:
        session.rollback()
        raise

def delete(identity):
    try:
        book = session.get(Book, {"id": identity})

        if not book:
            click.echo("Not Found")
            return

        session.delete(book)
        session.commit()
    except:
        session.rollback()
        raise
