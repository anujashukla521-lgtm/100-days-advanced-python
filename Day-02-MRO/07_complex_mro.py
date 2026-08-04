class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B):
    def show(self):
        print("D")
        super().show()

class E(B):
    def show(self):
        print("E")
        super().show()

class F(C):
    def show(self):
        print("F")
        super().show()

class G(D, E, F):
    def show(self):
        print("G")
        super().show()

G().show()
print(G.mro())

