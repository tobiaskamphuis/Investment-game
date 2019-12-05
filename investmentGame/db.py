from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

def db_engine_creation():
    # find current working directory
    cwd = os.getcwd()
    # latest folder in working directory
    last_folder = os.path.basename(os.path.normpath(cwd))
    if last_folder == 'investment game':
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        engine = create_engine('sqlite:///investmentGame/investmentGame.sqlite', echo=False)
    elif last_folder == 'investmentGame':
        print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
        engine = create_engine('sqlite:///investmentGame.sqlite', echo=False)
    session_factory = sessionmaker(bind=engine)
    return engine, session_factory






