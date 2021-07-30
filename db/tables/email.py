from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base


class Email(Base):
    __tablename__ = 'emails'

    id = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(String(50), nullable=False)
    user_login = Column(String(50),
                        ForeignKey('users.login',
                                   ondelete='CASCADE',
                                   onupdate='CASCADE'),
                        nullable=False)

    login = relationship('User')
