from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base


class FilmGenre(Base):
    __tablename__ = 'film_genres'

    film_id = Column(Integer,
                     ForeignKey('films.id',
                                onupdate='CASCADE',
                                ondelete='CASCADE'),
                     primary_key=True)
    film_genre_id = Column(String(20),
                           ForeignKey('genres.id',
                                      ondelete='CASCADE',
                                      onupdate='CASCADE'),
                           primary_key=True)

