class Shape:
    def draw(self):
        print("Drawing Shape")

class ColorMixin:
    def draw(self):
        print("Applying Color")
        super().draw()

class BorderMixin:
    def draw(self):
        print("Applying Border")
        super().draw()

class ShadowMixin:
    def draw(self):
        print("Applying Shadow")
        super().draw()


class Rectangle(ColorMixin, BorderMixin, ShadowMixin, Shape):
    def draw(self):
        print("Drawing Rectangle")
        super().draw()

r = Rectangle()
r.draw()
print(Rectangle.mro())