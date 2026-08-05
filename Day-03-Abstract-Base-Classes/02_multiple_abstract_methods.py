from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def area(self,length, width):
        return length*width

    def perimeter(self,length,width):
        return 2*(length+width)

class Circle(Shape):
    def area(self,radius):
        return 3.14*radius*radius

    def perimeter(self, radius):
        return 2*3.14*radius

rect = Rectangle()
c = Circle()

l = float(input("Enter length: "))
w = float(input("Enter width: "))
r = float(input("Enter radius: "))

print("Area of rectangle:",rect.area(l,w))
print("Perimeter of rectangle:",rect.perimeter(l,w))
print("Area of circle:",c.area(r))
print("Perimeter of circle:",c.perimeter(r))