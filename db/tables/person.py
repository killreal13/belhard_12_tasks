from sqlalchemy import Column, String, Integer, DateTime
from ..base import Base


class Person(Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    birthday = Column(DateTime, nullable=False)
