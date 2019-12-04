from investmentGame.Order import Order
from investmentGame.Portfolio import Portfolio
from sqlalchemy import Column, Integer, String, Boolean
from investmentGame.db import Base, engine, session_factory


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    balance = Column(Integer)
    #portfolio = Portfolio()

    def transaction(self, order, quantity, investment):
        """"Make transaction"""
        o = Order(order, quantity, investment)
        transaction_amount, price, date = o.market_order()
        self.balance = self.balance - transaction_amount
        self.portfolio.add_transaction(order, quantity, investment, price, date)

    def deposit_money(self, amount):
        self.balance = self.balance + amount

    def withdraw_money(self, amount):
        self.balance = self.balance - amount
