from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base


class UserFavoriteFilm(Base):
    __tablename__ = 'user_favorite_films'

    user_login = Column(String(50),
                        ForeignKey('users.login', onupdate='CASCADE', ondelete='CASCADE'),
                        primary_key=True)
    film_id = Column(Integer,
                     ForeignKey('films.id', ondelete='CASCADE', onupdate='CASCADE'),
                     primary_key=True)

