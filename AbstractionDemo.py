"""
For Abstract class, we need to must follow the below 2 conditions:
1) Import ABC library from abc or inherit ABC in a class
2) Atleast one abstract method is created inside a class."""
from abc import ABC, abstractmethod
class Shape(ABC):   # abstract class
    @abstractmethod        # Abstract method
    def area(self):
        pass

    @abstractmethod         # # Abstract method
    def perimeter(self):
        pass
class Rectangle(Shape):         # Derived class
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):             ## Implementing the abstract methods
        return self.width * self.height

    def perimeter(self):        ## Implementing the abstract methods
        return 2 * (self.width + self.height)

# Derived class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implementing the abstract methods
    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Example usage
shapes = [Rectangle(10, 20), Circle(5)]

for shape in shapes:
    print(f"Area: {shape.area( )}, Perimeter: {shape.perimeter( )}")

