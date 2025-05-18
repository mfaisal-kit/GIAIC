from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes"""
    
    @abstractmethod
    def area(self):
        """Abstract method that must be implemented by subclasses"""
        pass


class Rectangle(Shape):
    """Concrete implementation of Shape for rectangles"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Implementation of abstract method"""
        return self.width * self.height

# Create a Rectangle (concrete implementation)
rectangle = Rectangle(5, 3)
print(f"Rectangle area: {rectangle.area()}") 