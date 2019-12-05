from datetime import date
from investmentGame.api import pricemax, pricemin, pricelatest, getprices

class Order:
    def __init__(self, order, order_type, quantity, investment):
        self.order = order
        self.order_type = order_type
        self.quantity = quantity
        self.investment = investment

    def execution_order(self, execution_price = 0):
        if self.order_type == 'market_order':
            """buy and sell at market price"""
            getprices(self.investment)
            price = pricelatest(self.investment) # get_price(investment)
            dt = date.today().strftime("%d/%m/%Y")
            return price * self.quantity, price, dt

        if self.order_type == 'limit_order':
            dt = date.today().strftime("%d/%m/%Y")
            if self.order == 'Buy':
                getprices(self.investment)
                price = pricemin(self.investment)  # retrieve minimum price in last week
                if execution_price >= price:
                    return price * self.quantity, price, dt
                elif execution_price < price:
                    return 'error'
            if self.order == 'Sell':
                getprices(self.investment)
                price = pricemax(self.investment)  # retrieve maximum price in last week
                if execution_price <= price:
                    return price * self.quantity, price, dt
                elif execution_price > price:
                    return 'error'

#
order1 = Order('Buy', 'market_order', 10, 'AAPL')

print(order1.quantity)
print(order1.investment)
print(order1.execution_order())

order2 = Order('Buy', 'limit_order', 10, 'AAPL')

print(order2.quantity)
print(order2.investment)
print(order2.execution_order(261))

