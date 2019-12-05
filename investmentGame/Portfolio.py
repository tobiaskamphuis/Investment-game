from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from investmentGame.db import Base


class Portfolio(Base):
    __tablename__ = "portfolios"
    id = Column(Integer, primary_key=True)
    portfolio = Column(String)
    order = Column(String)
    quantity = Column(Integer)
    order_type = Column(String)
    investment = Column(Integer)
    price = Column(Integer)
    date = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="portfolios")


    # def add_transaction(self, order, quantity, investment, price, date):
    #     self.portfolio.append([order, quantity, investment, price, date])

    # def store_transactions(self):
    #     pd.DataFrame(self.portfolio).to_csv("transactions.csv")
