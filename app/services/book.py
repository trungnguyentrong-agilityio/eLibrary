from app.database import sqlalchemy_session
from app.models.book import Book
from app.database import connection_string

session = sqlalchemy_session(connection_string)

def list_books():
    for book in session.query(Book).all():
        print(f"book: {book}")

def create_book(profile_id):
    try:
        book = Book()
        book.profile_id = profile_id
        session.add(book)
        session.commit()
    except:
        session.rollback()
        raise

def update_book(id, book):
    # TODO: need to catch the missing id case (currently it doesn't show any error)
    try:
        session.query(Book).filter(Book.id == id).update({"status": book.status, "due_date": book.due_date, "profile_id": book.profile_id, "user_id": book.user_id})
        session.commit()
    except:
        session.rollback()
        raise

def delete_book(id):
    # TODO: need to catch the missing id case (currently it doesn't show any error)
    try:
        session.query(Book).filter(Book.id == id).delete()
        session.commit()
    except:
        session.rollback()
        raise
