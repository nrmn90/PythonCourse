import random
import sys

class Portfolio:

    def __init__(self):  # initialization of portfolio class
        self.portfolio_cash = 0  # starting portfolio is zero
        self.portfolio_stock = {}
        self.portfolio_mutualfund = {}
        self.stock = {}
        self.mutualfund = []
        self.hist = []

    def get_portfolio(self):
        print('You have', self.portfolio_cash, 'cash')
        print('Your stock portfolio is:', self.portfolio_stock)
        print('Your mutual fund portfolio is:', self.portfolio_mutualfund)

    def add_cash(self):
        amount = int(input('How many cash you want to add?'))
        self.portfolio_cash += amount
        print('You have', self.portfolio_cash, 'cash')
        self.hist.append(('Added cash', amount))

    def withdraw_cash(self):
        amount = int(input('How many cash you want to withdraw?'))
        self.portfolio_cash -= amount
        print('You have', self.portfolio_cash, 'cash')
        self.hist.append(('Withdrawn', amount))

    # Stock part
    def add_stock(self):  # adding stock(s) to the buy list
        s = int(input('How many stocks you want to insert?'))
        for i in range(s):
            text = input('First enter stock symbol and then price: ').split()
            self.stock[text[0]] = text[1]

    def buy_stock(self):
        t = list(self.stock.items())
        for stk, prc in enumerate(t):  # Returns both the index and the value of each element
            print(stk + 1, '-', prc)
        choice = int(input('Choose from available stocks above'))
        share = int(input('insert the number of shares you want to buy'))
        self.portfolio_cash -= share * int(t[choice - 1][1])
        self.portfolio_stock[t[choice - 1][0]] = share
        print("You bought", share, 'shares of', t[choice - 1][0], 'and it costed', share * int(t[choice - 1][1]))
        print('You have', self.portfolio_cash, 'cash')
        self.hist.append(('Bought:', t[choice - 1][0], share))

    def sell_stock(self):
        t = list(self.stock.items())
        ps = list(self.portfolio_stock.items())
        for stk, prc in enumerate(t):  # Returns both the index and the value of each element
            print(stk + 1, '-', prc)
        choice = int(input('Choose from available stocks above'))
        share = int(input('insert the number of shares you want to sell'))
        self.portfolio_cash += share * random.uniform(0.5 * int(t[choice - 1][1]), 1.5 * int(t[choice - 1][1]))
        self.portfolio_stock[t[choice - 1][0]] = self.portfolio_stock[t[choice - 1][0]] - share
        print("You sold", share, 'shares of', t[choice - 1][0], 'and it costed',
              share * random.uniform(0.5 * int(t[choice - 1][1]), 1.5 * int(t[choice - 1][1])))
        print('You have', self.portfolio_cash, 'cash')
        self.hist.append(('Sold:', t[choice - 1][0], share))

    # Mutual funds part
    def add_mutualfund(self):  # adding mutual fund(s) to the buy list
        m = int(input('How many mutual funds you want to insert?'))
        for i in range(m):
            text = input('Enter the symbol of the mutual funds: ')
            self.mutualfund.append(text)

    def buy_mutualfund(self):
        for i, m in enumerate(self.mutualfund):
            print(i + 1, '-', m)
        choice = int(input('Choose from available mutual funds above'))
        share = int(input('insert the number of shares of chosen mutual fund to buy'))
        self.portfolio_cash -= share * 1
        self.portfolio_mutualfund[self.mutualfund[choice - 1]] = share
        print("You bought", share, 'shares of', self.mutualfund[choice - 1], 'and it costed', share * 1)
        print('You have', self.portfolio_cash, 'cash')
        self.hist.append(('Bought:', self.mutualfund[choice - 1], share))

    def sell_mutualfund(self):
        for i, m in enumerate(self.mutualfund):
            print(i + 1, '-', m)
        choice = int(input('Choose from available mutual funds above'))
        share = int(input('insert the number of shares of chosen mutual fund to sell'))
        self.portfolio_cash += share * 1
        self.portfolio_mutualfund[self.mutualfund[choice - 1]] = self.portfolio_mutualfund[
                                                                     self.mutualfund[choice - 1]] - share
        print("You sold", share, 'shares of', self.mutualfund[choice - 1], 'and it costed',
              share * random.uniform(0.9, 1.2))
        print('You have', self.portfolio_cash, 'cash')
        self.hist.append(('Sold:', self.mutualfund[choice - 1], share))

    def history(self):
        for i, h in enumerate(self.hist):
            print(i + 1, '-', h)


p = Portfolio()


def menu():
    while True:
        print('''Please, select from available options:
                  1. Add or withdraw cash 
                  2. Insert stock list for portfolio
                  3. Buy or sell stock(s) from created list
                  4. Insert mutual fund list for portfolio
                  5. Buy or sell mutual fund(s) from created list
                  6. Exit and show history of transactions''')
        menu_option = int(input())
        if menu_option == 1:
            print('Press 1. to add cash and 2. to withdraw cash')
            sub_menu = int(input())
            if sub_menu == 1:
                p.add_cash()
            elif sub_menu == 2:
                p.withdraw_cash()
            print()
            menu()
        elif menu_option == 2:
            p.add_stock()
            print()
            menu()
        elif menu_option == 3:
            print('Type 1 to buy and 2 to sell stock(s)')
            sub_menu = int(input())
            if sub_menu == 1:
                p.buy_stock()
            elif sub_menu == 2:
                p.sell_stock()
            print()
            menu()
        elif menu_option == 4:
            p.add_mutualfund()
            print()
            menu()
        elif menu_option == 5:
            print('Type 1 to buy and 2 to sell mutual fund(s)')
            sub_menu = int(input())
            if sub_menu == 1:
                p.buy_mutualfund()
            elif sub_menu == 2:
                p.sell_mutualfund()
            print()
            menu()
        elif menu_option == 6:
            print('Here are your transactions below')
            p.history()
            sys.exit()
menu()