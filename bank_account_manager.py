class Account:
    def __init__(self, acct_nbr, opening_deposit ):
        self.acct_nbr = acct_nbr
        self.balance = opening_deposit

    def __str__(self):
        return f'${self.balance:.2f}'
        # DEFINE A UNIVERSAL METHOD TO ACCEPT DEPOSITS

    def deposit(self, dep_amt):
        self.balance = self.balance + dep_amt

        # DEFINE A UNIVERSAL METHOD TO ACCEPT WITHDRAWALS

    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
        else:
            print('Funds unavailable!')


class Checking(Account):
    def __init__(self, acct_nbr, opening_deposit):
        super().__init__(acct_nbr, opening_deposit)

    # DEFINE A STRING METHOD
    def __str__(self):
        return f'Checking Account #{self.acct_nbr}\n Balance:{Account.__str__(self)}'


class Saving(Account):
    def __init__(self, acct_nbr,opening_deposit):
        super().__init__(acct_nbr, opening_deposit)

    # DEFINE A STRING METHOD
    def __str__(self):
        return f'Saving Account #{self.acct_nbr}\n Balance:{Account.__str__(self)}'

class Business(Account):
    def __init__(self, acct_nbr, opening_deposit):
        super().__init__(acct_nbr, opening_deposit)

    # DEFINE A STRING METHOD
    def __str__(self):
        return f'Business Account #{self.acct_nbr}\n Balance:{Account.__str__(self)}'


class Customer:
    def __init__(self, cust_name, cust_pin):
        self.cust_name = cust_name
        self.cust_pin = cust_pin
        # Create a dictionary of accounts with lists to hold multiple accounts
        self.accts = {'C': [], 'S': [], 'B': []}

    def __str__(self):
        return self.cust_name

    def open_checking(self, acct_nbr, opening_deposit):
        self.accts['C'].append(Checking(acct_nbr,opening_deposit))

    def open_saving(self, acct_nbr, opening_deposit):
        self.accts['S'].append(Saving(acct_nbr, opening_deposit))

    def open_business(self, acct_nbr, opening_deposit):
        self.accts['B'].append(Business(acct_nbr, opening_deposit))

    # rather than maintain a running total of deposit balances
    # write a method that computes a total as needed
    def get_total_deposit(self):
        total = 0
        for acct in self.accts['C']:
            print(acct)
            total = total + acct.balance
        for acct in self.accts['S']:
            print(acct)
            total = total + acct.balance
        for acct in self.accts['B']:
            print(acct)
            total = total + acct.balance
        print(f'Combined Deposits: ${total:.2f}')

    # write some functions for making deposits and withdrawals


def make_dep(cust, acct_type, acct_num, dep_amt):
    for acct in cust.accts[acct_type]:
        if acct.acct_nbr == acct_num:
            acct.deposit(dep_amt)


def make_wd(cust, acct_type, acct_num, wd_amt):
    for acct in cust.accts[acct_type]:
        if acct.acct_nbr == acct_num:
            acct.withdraw(wd_amt)

nancy=Customer("Nancy",2)
nancy.open_business(2018,8900)
nancy.get_total_deposit()
make_dep(nancy,'B',2018,100)
nancy.get_total_deposit()
make_wd(nancy,'B',2018,1000000)
nancy.get_total_deposit()










