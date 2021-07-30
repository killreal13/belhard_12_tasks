from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base


class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, autoincrement=True, primary_key=True)
    duration = Column(Integer, nullable=False)
    name = Column(String(50), nullable=False)
    release_date = Column(DateTime, nullable=False)
    rating = Column(Float, nullable=False)
    director_id = Column(Integer,
                         ForeignKey('persons.id',
                                    onupdate='CASCADE',
                                    ondelete='CASCADE'),
                         nullable=False)
    genre = relationship('Genre',
                         secondary='film_genres',
                         backref='film',
                         cascade='all, delete',
                         passive_deletes=True)
    director = relationship('Person')
