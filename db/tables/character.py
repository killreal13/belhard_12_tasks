from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base


class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(15), nullable=False)
    comment = Column(String(150))
    film_id = Column(Integer, ForeignKey('films.id',
                                         onupdate='CASCADE',
                                         ondelete='CASCADE'),
                     nullable=False)

    favorite_film = relationship('Person',
                                 secondary='characters_actors',
                                 backref='character',
                                 cascade='all, delete',
                                 passive_deletes=True
                                 )
    film = relationship('Film')
