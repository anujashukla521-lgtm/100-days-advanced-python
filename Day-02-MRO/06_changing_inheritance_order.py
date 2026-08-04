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
        print("D")
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


class D(C, B):
    def display(self):
        print("D")
# [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

D().display()
print(D.mro())