# polymorphism_demo.py
import math  # Ensure this import is here to use math.pi for Circle's area calculation

class Shape:
    def __init__(self) -> None:
        pass

    def area(self):
        raise NotImplementedError("This method must be implemented by subclasses")

class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  

class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2  
