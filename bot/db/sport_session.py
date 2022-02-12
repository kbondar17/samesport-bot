import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from bot.loader import config

SQLALCHEMY_DATABASE_URI = config['SQLALCHEMY_DATABASE_URI']

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

engine = create_engine(SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(sessionmaker(bind=engine))

Base = automap_base()
Base.prepare(engine, reflect=True)

# wp_usermeta = Base.classes.wp_usermeta
# db_session.query(wp_usermeta).first().meta_key
