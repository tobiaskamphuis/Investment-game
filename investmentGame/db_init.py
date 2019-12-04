from investmentGame.User import User
from investmentGame.db import Base, engine, session_factory
from sqlalchemy.sql import exists

def db_init():

    Base.metadata.create_all(engine)

    u1 = User(name='Esther', age=26, balance=0)
    u2 = User(name='Jeroen', age=26, balance=0)
    u3 = User(name='Tobias', age=26, balance=0)
    session = session_factory()
    session.add(u1)
    session.add(u2)
    session.add(u3)

    session.commit()


#db_init()

session = session_factory()

#for instance in session.query(User).filter(User.name == 'Jeroen'):
#    instance.balance += 150
#    session.commit()


nm = 'Jeroen'

i = session.query(User).filter(User.name == nm).first()
print(i)

#print(i.name, i.balance)





