from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    def display_balance(self):
        print(f"Current balance: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance+=amount
            print("Deposited:",amount)
            self.display_balance()
        else:
            print("Invalid deposit amount")

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print("Withdrawn:",amount)
            self.display_balance()
        else:
            print("Insufficient balance")
    
class CurrentAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        OVERDRAFT_LIMIT = 5000
        if amount <= self.balance + OVERDRAFT_LIMIT and amount > 0:
            self.balance -= amount
            print("Withdrawn:",amount)
            self.display_balance()
        else:
            print("Overdraft Limit Exceeded")



b = int(input("Enter current balance: "))

s_acc = SavingsAccount(b)
d = int(input("Enter amount to deposit: "))
w = int(input("Enter amount to withdraw: "))
print("SAVINGS ACCOUNT")
print("-"*40)
s_acc.display_balance()
s_acc.deposit(d)
s_acc.withdraw(w)

c_acc = CurrentAccount(b)
d = int(input("Enter amount to deposit: "))
w = int(input("Enter amount to withdraw: "))
print("CURRENT ACCOUNT")
print("-"*40)
c_acc.display_balance()
c_acc.deposit(d)
c_acc.withdraw(w)


