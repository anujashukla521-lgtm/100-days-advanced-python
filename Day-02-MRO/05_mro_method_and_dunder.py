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

for class_name in D.mro():
    print(class_name)

for class_name in D.__mro__:
    print(class_name)
