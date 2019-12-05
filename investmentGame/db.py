from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


# find current working directory
cwd = os.getcwd()
# directory of the script being run
#
os.path.dirname(os.path.abspath(__file__))

Base = declarative_base()
engine = create_engine('sqlite:///investmentGame.sqlite', echo=False)
session_factory = sessionmaker(bind=engine)


