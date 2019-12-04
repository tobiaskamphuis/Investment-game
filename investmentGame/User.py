from investmentGame.Order import Order
from investmentGame.Portfolio import Portfolio


class User:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance
        self.portfolio = Portfolio()

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


p1 = User("John", 36, 10000)
p1.transaction('Sell', 'market_order', 10, 'x')
p1.transaction('Buy', 'limit_order',  20, 'y', 150, '12/04/2019')
p1.portfolio.store_transactions()

print(p1.balance)
print(p1.name)
print(p1.portfolio.portfolio)