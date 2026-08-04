class A:
    def display(self):
        print("A")

class B(A):
    def display(self):
        print("B")

class C(A):
    def display(self):
        print("C")

class D(B, C):
    def display(self):
        pass

D().display()
print(D.mro())