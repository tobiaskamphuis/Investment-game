from datetime import datetime


class Order:
    def __init__(self, order, quantity, investment):
        self.order = order
        self.quantity = quantity
        self.investment = investment

    def market_order(self):
        """make market
        """
        price = 150 #get_price(investment)

        now = datetime.now()
        dt = now.strftime("%m/%d/%Y, %H:%M:%S")
        return price * self.quantity, price, dt

