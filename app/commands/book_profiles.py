from app.database import sqlalchemy_session
from app.models.book_profile import BookProfile
from app.database import connection_string

session = sqlalchemy_session(connection_string)

def list_book_profiles():
    for author, title in session.query(BookProfile.author, BookProfile.title).all():
        print(f"Author: {author} - Title: {title}")

def create_book_profile(author, title):
    try:
        profile = BookProfile(author = author, title = title)

        session.add(profile)
        session.commit()
    except:
        print("Error when create book profile")
        session.rollback()
        raise

def update_book_profile(id, profile):
    # TODO: need to catch the missing id case (currently it doesn't show any error)
    try:
        session.query(BookProfile).filter(BookProfile.id == id).update({"title": profile.title, "author": profile.author})
        session.commit()
    except:
        print("Error when update book profile")
        session.rollback()
        raise

def delete_book_profile(id):
    # TODO: need to catch the missing id case (currently it doesn't show any error)
    try:
        session.query(BookProfile).filter(BookProfile.id == id).delete()
        session.commit()
    except:
        print("Error when delete book profile")
        session.rollback()
        raise
