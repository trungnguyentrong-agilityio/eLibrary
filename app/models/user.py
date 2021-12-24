from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String

from .base import Base


class User(Base):
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    book = relationship("Book")
