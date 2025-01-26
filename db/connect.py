from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:root@localhost/py-flask")

session = scoped_session(sessionmaker(engine))

Base = declarative_base()