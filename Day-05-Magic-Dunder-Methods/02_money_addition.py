class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        return self.amount + other.amount

m1 = Money(500, "INR")
m2 = Money(300, "INR")
print(m1+m2)