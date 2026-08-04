class X:
    def __init__(self):
        super().__init__()
        print("Class X")

class Y:
    def __init__(self):
        super().__init__()
        print("Class Y")

class Z(X, Y):
    def __init__(self):
        super().__init__()
        print("Class Z")

z = Z()
print(Z.mro())