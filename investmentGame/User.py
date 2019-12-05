from investmentGame.Order import Order
from investmentGame.Portfolio import Portfolio
from sqlalchemy import Column, Integer, String, Boolean
from investmentGame.db import Base, engine, session_factory


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    age = Column(Integer)
    balance = Column(Integer)
    #portfolio = Portfolio()

    def transaction(self, order, order_type, quantity, investment, execution_price = 0, execution_date = 0):
        """"Make transaction"""
        o = Order(order, order_type, quantity, investment)
        transaction_amount, price, date = o.execution_order(execution_price, execution_date)
        self.balance = self.balance - transaction_amount
        self.portfolio.add_transaction(order, quantity, investment, price, date)

    def deposit_money(self, amount):
        self.balance = self.balance + amount

    def withdraw_money(self, amount):
        self.balance = self.balance - amount
