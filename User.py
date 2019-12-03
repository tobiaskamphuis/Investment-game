from Order import Order

class User:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance
        self.portfolio = []

    def make_portfolio(self):
        """Make a portfolio"""

    def transaction(self, order, quantity, investment):
        """"Make transaction"""
        o = Order(order, quantity, investment)
        transaction_amount = o.market_order()
        self.balance = self.balance - transaction_amount

        #if transaction_status == True:
        #    update_portfolio()
        #else:
        #    return error

    def deposit_money(self, amount):
        self.balance = self.balance + amount

    def withdraw_money(self, amount):
        self.balance = self.balance - amount


p1 = User("John", 36, 10000)

print(p1.balance)
p1.transaction(1, 10, 'x')
print(p1.name)
print(p1.age)
print(p1.balance)