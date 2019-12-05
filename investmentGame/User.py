from investmentGame.Order import Order
from investmentGame.Portfolio import Portfolio
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    age = Column(Integer)
    balance = Column(Integer)
    portfolios = relationship("Portfolio", order_by=Portfolio.id, back_populates="user")

    def transaction(self, order, order_type, quantity, investment, execution_price=0, execution_date=0):
        """"Make transaction"""
        o = Order(order, order_type, quantity, investment)
        transaction_amount, price, date = o.execution_order(execution_price, execution_date)
        self.balance = self.balance - transaction_amount
        return transaction_amount, price, date

    def deposit_money(self, amount):
        self.balance = self.balance + amount

    def withdraw_money(self, amount):
        self.balance = self.balance - amount


#User(name='Jeroen', age=26, balance=20)#, password='Welcome'


#u.transaction('buy', 'market_order', 20, 1)