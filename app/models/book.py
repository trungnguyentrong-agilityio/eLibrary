import enum

from sqlalchemy import ForeignKey
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String, Enum, DateTime, Integer

from .base import Base


class BookStatus(enum.Enum):
    available = "available"
    unavailable = "unavailable"


class Book(Base):
    status = Column(Enum(BookStatus), nullable=False)
    due_date = Column(DateTime)
    profile_id = Column(Integer, ForeignKey("book_profiles.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __init__(self):
        self.status = BookStatus.available.value
    def __repr__(self):
        return "<Book(status='{}', due_date='{}', profile_id={}, user_id={}, created_at={}, updated_at={} )>"\
                .format(self.status, self.due_date, self.profile_id, self.user_id, self.created_at, self.updated_at)
