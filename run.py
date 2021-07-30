import datetime

from db import session_scope
from db import tables
import datetime


with session_scope() as session:
    person = tables.Person(
        name='jon',
        surname='snow',
        birthday=datetime.date.today()
    )
    session.add(person)
    session.commit()
    genre = session.query(tables.Genre).filter_by(name='Crime').one()
    session.delete(genre)
    session.commit()
    result = session.query(tables.User).all()
    print(result)
    users = session.query(tables.User).filter_by(person_id='1').one()
    users.password = 'nwqewqee'
    session.commit()
