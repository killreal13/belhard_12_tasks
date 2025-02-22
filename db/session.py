from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

engine = create_engine(
    "mysql+pymysql://root:5534097asd@localhost:3306/film_zone",
    pool_pre_ping=True,
    pool_recycle=3600,
)
Session = sessionmaker(bind=engine, autocommit=False)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

