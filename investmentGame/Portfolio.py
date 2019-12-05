import pandas as pd


class Portfolio:
    def __init__(self):
        self.portfolio = []

    def add_transaction(self, order, quantity, investment, price, date):
        self.portfolio.append([order, quantity, investment, price, date])

    def store_transactions(self):
        pd.DataFrame(self.portfolio).to_csv("transactions.csv")