from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base


class User(Base):
    __tablename__ = 'users'

    login = Column(String(20), primary_key=True)
    password = Column(String(45), nullable=False)
    user_type_id = Column(String(20),
                          ForeignKey('user_types.id', onupdate='CASCADE', ondelete='CASCADE'),
                          nullable=False)
    person_id = Column(Integer,
                       ForeignKey('persons.id', ondelete='CASCADE', onupdate='CASCADE'),
                       nullable=False)
    favorite_film = relationship('Film',
                                 secondary='user_favorite_films',
                                 backref='users_favorites',
                                 cascade='all, delete',
                                 passive_deletes=True
                                 )

    user_type = relationship('UserType')
    person = relationship('Person')

    def __repr__(self):
        return f'<User login: {self.login}, user type: {self.user_type_id}>'