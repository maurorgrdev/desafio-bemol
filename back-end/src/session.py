from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("mysql+pymysql://root:@localhost/street")
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

def get_session():
    return Session()