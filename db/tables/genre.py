from sqlalchemy import Column, String
from ..base import Base


class Genre(Base):
    __tablename__ = 'genres'

    id = Column(String(30), primary_key=True)
    name = Column(String(30), nullable=False)