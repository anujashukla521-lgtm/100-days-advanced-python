class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def __str__(self):
        return f"Account holder {self.owner} has balance Rs.{self.balance}"

    def __add__(self, other):
        return self.balance + other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __len__(self):
        return len(self.transactions)

    def __getitem__(self, key):
        return self.transactions[key]

acc1 = BankAccount("Rohan", 25000)
acc2 = BankAccount("Rahul", 25500)

acc1.transactions.append("Deposited Rs.5000")
acc1.transactions.append("Withdrawn Rs.2000")

acc2.transactions.append("Deposited Rs.3000")

print(acc1)
print(acc2)
print(acc1 + acc2)
print(acc1 > acc2)
print(acc1 == acc2)
print(len(acc1))
print(len(acc2))
print(acc1[0])