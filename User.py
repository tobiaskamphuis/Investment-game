from Order import Order
from Portfolio import Portfolio

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
        #if transaction_status == True:
        self.portfolio.add_transaction(order, quantity, investment, price, date)
        #else:
        #    return error

    def deposit_money(self, amount):
        self.balance = self.balance + amount

    def withdraw_money(self, amount):
        self.balance = self.balance - amount


p1 = User("John", 36, 10000)

print(p1.balance)
p1.transaction('Sell', 10, 'x')
p1.transaction('Buy', 20, 'y')
print(p1.name)

print(p1.portfolio.portfolio)


stock_indx = ['x', 'y', 'i', 'sdfaa']

print('www.xyz.com/mystock=%s' % (stock_indx[3]) )