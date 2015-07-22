import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from settings import DATABASE, TABLE_NAME

DeclarativeBase = declarative_base()

"""
def db_connect():
    return create_engine('mysql+mysqldb://root:root@localhost:3306/jobs?charset=utf8', encoding='utf-8')
"""
def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**DATABASE))    

def create_jobsdb_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class Jobsdb(DeclarativeBase):
    __tablename__ =  TABLE_NAME

    id = Column(Integer, primary_key=True)
    title = Column('title', String(500))
    link = Column('link', String(500))
    time = Column('time', String(500))
    created_date = Column(DateTime, default=datetime.datetime.now())
