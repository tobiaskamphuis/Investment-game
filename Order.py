import datetime

class Order:
    def __init__(self, order, quantity, investment):
        self.order = order
        self.quantity = quantity
        self.investment = investment

    def market_order(self):
        """make market
        """
        price = 150 #get_price(investment)
        dt = datetime.datetime.now()
        return price * self.quantity, price, dt


order = Order('market_order', 10, 'SMA')

print(order.quantity)
print(order.investment)
print(order.market_order())
