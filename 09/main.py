from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method has no implementation

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Trying to create a Shape object will raise an error:
# shape = Shape()  # This will raise TypeError: Can't instantiate abstract class Shape

# Create a Rectangle object and use area()
rect = Rectangle(5, 3)
print("Area of rectangle:", rect.area())
