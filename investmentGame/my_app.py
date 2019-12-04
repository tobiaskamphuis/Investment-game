from investmentGame.User import User
from investmentGame.db import Base, engine, session_factory


if __name__ == '__main__':
    print('Welcome to my investment game\n')

    session = session_factory()
    input_user = input('Please enter your user name: ')
    i = session.query(User).filter(User.name == input_user).first()

    if i is not None:
        print('correct')
        user_validation = 'correct'
    else:
        print('Not a valid user')
        user_validation = 'incorrect'

    if user_validation == 'correct':
        p1 = i
        print('Hi %s, what would you like to do? \nd = deposit, w = withdraw, i = invest, q = quit' % p1.name)

        while 1 == 1:
            print('Your current balance = %i' % p1.balance)
            i = input('Input: ')

            if i == 'd':
                deposit = input('Amount deposit: ')
                p1.deposit_money(int(deposit))
                session.commit()

            elif i == 'w':
                withdraw = input('Amount withdraw: ')
                p1.withdraw_money(int(withdraw))
                session.commit()

            elif i == 'i':
                print('invest')

            elif i == 'q':
                # Store current state of account in database
                break
