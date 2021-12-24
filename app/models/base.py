from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, DateTime, Integer, MetaData
from inflection import tableize


class Base:
    @declared_attr
    def __tablename__(self):
        return tableize(self.__name__)

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(
        DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow
    )


appMetaData = MetaData()
Base = declarative_base(metadata=appMetaData, cls=Base)
