class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
        else:
            print('Insufficient Funds: Charging a $5 Fee.')
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_intrest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

checking = BankAccount(.02, 500)
savings = BankAccount(.07, 700)

checking.deposit(50).deposit(350).deposit(500).withdraw(100).yield_intrest().display_account_info()
savings.deposit(4000).deposit(500).withdraw(50).withdraw(50).withdraw(25).withdraw(25).yield_intrest().display_account_info()

