class A:
    def display(self):
        print("A")

class B(A):
    def display(self):
        print("B")
        super().display()

class C(A):
    def display(self):
        print("C")
        super().display()

class D(B, C):
    def display(self):
        print("D")
        super().display()

D().display()
print(D.mro())