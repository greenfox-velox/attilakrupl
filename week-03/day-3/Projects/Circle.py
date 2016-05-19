# Create a `Circle` class that takes it's radius as cinstructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area
import math

class Circle:
    
    def __init__(self, x):
        self.radius = x
        
        
    def get_circumference(self):
        circumference = self.radius * 2 * math.pi
        return circumference
    
    def get_area(self):
        area = self.radius ** 2 * math.pi
        return area
    
    
kiskor = Circle(5)

print(kiskor.get_circumference())
print(kiskor.get_area())

    
    
        