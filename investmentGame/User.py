from investmentGame.Order import Order
from investmentGame.Portfolio import Portfolio

class User:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance
        self.portfolio = Portfolio()

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


p1 = User("John", 36, 10000)
p1.transaction('Sell', 10, 'x')
p1.transaction('Buy', 20, 'y')
p1.portfolio.store_transactions()



print(p1.balance)
print(p1.name)
print(p1.portfolio.portfolio)