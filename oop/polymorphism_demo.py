import math


class Shape:
    def __init__(self) -> None:
        pass

    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self,radius) -> None:
        super().__init__()
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius


