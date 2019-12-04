from datetime import date

class Order:
    def __init__(self, order, order_type, quantity, investment):
        self.order = order
        self.order_type = order_type
        self.quantity = quantity
        self.investment = investment

    def market_order(self):
        """buy and sell at market price"""
        price = 150 #get_price(investment)
        dt = date.today().strftime("%d/%m/%Y")
        return price * self.quantity, price, dt

    def limit_order(self, execution_price, order_date):
        """buy till max price or sell from min price during timeframe"""
        """ limit order checks if price on order date """
        """ require to retrieve minimum and maximum price in last week of stock"""
        dt = date.today().strftime("%d/%m/%Y")
        while order_date >= dt:
            if self.order == 'Buy':
                price = 150  # retrieve minimum price in last week
                if execution_price >= price:
                    return price * self.quantity, price, dt
                elif execution_price < price:
                    return 'error'
            if self.order == 'Sell':
                price = 150  # retrieve maximum price in last week
                if execution_price <= price:
                    return price * self.quantity, price, dt
                elif execution_price > price:
                    return 'error'


order1 = Order('Buy', 'market_order', 10, 'SMA')

print(order1.quantity)
print(order1.investment)
print(order1.market_order())

order2 = Order('Buy', 'limit_order', 10, 'SMA')

print(order2.quantity)
print(order2.investment)
print(order2.limit_order(140, '04/12/2019'))
