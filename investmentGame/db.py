from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine('sqlite:///investmentGame.sqlite', echo=False)
session_factory = sessionmaker(bind=engine)


