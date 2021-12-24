from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String

from .base import Base


class BookProfile(Base):
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    book = relationship("Book")
