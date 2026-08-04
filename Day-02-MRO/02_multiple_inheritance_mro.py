class Father:
    def show(self):
        print("Father")

class Mother:
    def show(self):
        print("Mother")

class Child(Father, Mother):
    pass

Child().show()
print(Child.mro())