from investmentGame.User import User
from investmentGame.User import Portfolio
from investmentGame.db import Base, engine, session_factory


if __name__ == '__main__':
    print('Welcome to my investment game\n')

    session = session_factory()
    input_user = input('Please enter your user name: ')
    user = session.query(User).filter(User.name == input_user).first()

    if user is not None:
        print('correct')
        user_validation = 'correct'
    else:
        print('Not a valid user')
        user_validation = 'incorrect'

    if user_validation == 'correct':
        print('Hi %s, what would you like to do? \nd = deposit, w = withdraw, i = invest, p = portfolio, q = quit'
              % user.name)

        while 1 == 1:
            print('Your current balance = %i' % user.balance)
            i = input('Input: ')

            if i == 'd':
                deposit = input('Amount deposit: ')
                user.deposit_money(int(deposit))
                session.commit()

            elif i == 'w':
                withdraw = input('Amount withdraw: ')
                user.withdraw_money(int(withdraw))
                session.commit()

            elif i == 'p':
                for portfolio in user.portfolios:
                    print(portfolio.portfolio, portfolio.quantity, portfolio.order)

            elif i == 'i':
                print('What would you like to order? ')
                portfolio = input("Portfolio: ")
                order = input('Order Input: ')
                order_type = input('Order Typ Input: ')
                quantity = input('quantity Input: ')
                investment = input('investment Input: ')

                transaction_amount, price, date = user.transaction(order, 'market_order', quantity, 'x')

                p = Portfolio(portfolio=portfolio, order=order, quantity=quantity, order_type=order_type,
                              investment=investment, price=price, date=date, user=user)
                session.commit()

            elif i == 'q':
                # Store current state of account in database
                break
