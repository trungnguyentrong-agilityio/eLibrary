import click
from app.database import sqlalchemy_session
from app.models.book_profile import BookProfile
from app.database import connection_string
from app.serializers import BookProfileSchema

session = sqlalchemy_session(connection_string)

def get_all():
    try:
        book_profile = session.query(BookProfile).all()

        return BookProfileSchema().dumps(book_profile, many=True)
    except:
        session.rollback()
        raise

def get_one(identity: int):
    try:
        book_profile = session.get(BookProfile, {"id": identity})

        if not book_profile:
            click.echo("Not Found")
            return

        return BookProfileSchema().dumps(book_profile)
    except:
        session.rollback()
        raise

def create(author: str, title: str):
    try:
        profile = BookProfile(author = author, title = title)

        session.add(profile)
        session.commit()

        return BookProfileSchema().dumps(profile)
    except:
        session.rollback()
        raise

def update(identity: int, author: str, title: str):
    try:
        profile = session.get(BookProfile, {"id": identity})

        if not profile:
            click.echo("Not Found")
            return

        profile.author = author
        profile.title = title
        session.commit()

        return BookProfileSchema().dumps(profile)
    except:
        session.rollback()
        raise

def delete(identity):
    try:
        profile = session.get(BookProfile, {"id": identity})

        if not profile:
            click.echo("Not Found")
            return

        session.delete(profile)
        session.commit()
    except:
        session.rollback()
        raise
