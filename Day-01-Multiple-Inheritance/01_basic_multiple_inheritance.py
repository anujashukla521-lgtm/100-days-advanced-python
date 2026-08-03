class Father:
    def programming(self):
        print("Father knows Python")

class Mother:
    def painting(self):
        print("Mother is a good painter")

class Child(Father,Mother):
    pass


c = Child()
c.programming()
c.painting()