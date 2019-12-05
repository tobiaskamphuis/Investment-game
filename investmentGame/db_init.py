from investmentGame.User import User
from investmentGame.Portfolio import Portfolio
from sqlalchemy.ext.declarative import declarative_base
from investmentGame.db import db_engine_creation, Base

engine, session_factory = db_engine_creation()

def db_init():

    Base.metadata.create_all(engine)

    u1 = User(name='Esther', password='Welcome', age=26, balance=0)#, password='Welcome'
    u2 = User(name='Jeroen', password='Welcome', age=26, balance=1000)
    u3 = User(name='Tobias', password='Welcome', age=26, balance=0)

    p1 = Portfolio(portfolio = 'x', order = 'Buy', quantity = 10, order_type = 'market_order'
    , investment = 'STOCK_TYPE', price = 100, date = 'DATE_NOW', user = u2)

    session = session_factory()
    session.add(u1)
    session.add(u2)
    session.add(u3)
    session.add(p1)
    # session.add(p2)
    # session.add(p3)
    # session.add(p4)
    session.commit()


db_init()



# for instance in session.query(User).filter(User.name == 'Esther'):
#     for i in instance.portfolios:
#         print(i.portfolio)
   # instance.balance += 150
   # session.commit()
#
# session = session_factory()
# nm = 'Esther'
#
# i = session.query(User).filter(User.name == nm).first()
# print(i.portfolios)
# p = Portfolio(portfolio='z', user=i, order='Buy', quantity=10)
#
# session.commit()
#
#
# session = session_factory()
# nm = 'Esther'
#
# i = session.query(User).filter(User.name == nm).first()
# print(i.portfolios)
#
#
#





