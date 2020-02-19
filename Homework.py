import random


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

    def add_cash(self, amount):
        self.portfolio_cash += amount
        print('You have', self.portfolio_cash, 'cash')
        self.hist.append(('Added cash', amount))

    def withdraw_cash(self, amount):
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
            print(i+1, '-', h)
