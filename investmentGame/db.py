from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


def db_engine_creation():
    # find current working directory
    cwd = os.getcwd()
    # latest folder in working directory
    last_folder = os.path.basename(os.path.normpath(os.path.dirname(cwd)))
    Base = declarative_base()
    if last_folder == 'investment game':
        engine = create_engine('sqlite:///investmentGame/db_engine.sqlite', echo=False)
    elif last_folder == 'investmentGame':
        engine = create_engine('sqlite:///db_engine.sqlite', echo=False)
    session_factory = sessionmaker(bind=engine)
    return Base, engine, session_factory






