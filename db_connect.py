from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

engine = create_engine(
    'mysql+pymysql://root:12042006tsts@localhost:3306/film_zone',
    pool_pre_ping=True,
    pool_recycle=3600,
)


def get_session():
    return sessionmaker(bind=engine)()


@contextmanager
def session_scope():
    session = get_session()()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()