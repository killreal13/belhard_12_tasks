from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base


class CharacterActor(Base):
    __tablename__ = 'characters_actors'

    character_id = Column(Integer,
                          ForeignKey('characters.id',
                                     onupdate='CASCADE',
                                     ondelete='CASCADE'),
                          primary_key=True)
    person_id = Column(Integer,
                       ForeignKey('persons.id',
                                  ondelete='CASCADE',
                                  onupdate='CASCADE'),
                       primary_key=True)
