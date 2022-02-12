from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from bot.loader import config

SQLALCHEMY_DATABASE_URI = config['SQLALCHEMY_DATABASE_URI']
engine = create_engine(SQLALCHEMY_DATABASE_URI)

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property



def create_db():
    Base.metadata.create_all(bind=engine)


def reset_db():
    for table in Base.metadata.sorted_tables:
        try:
            print('удаляем', table)
            table.drop(engine)
        except Exception as ex:
            print(table, ex)
