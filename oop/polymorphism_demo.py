#A script to demonstrate the understanding of overriding and polymorphic behaviour

#Create a base class called SHAPE with a method called area
class Shape:
    def __init__(self):
        return None  
    
    def area(self):
        raise NotImplementedError

#Derive a class to inherit from the parent class     
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        """The area method is redefine here to override the notimplemented error, 
    being that values would have been given exhibiting polymorphic behaviour."""
        return self.length * self.width     
  
#Derive another class Circle
import math         #Inorder to use the the pi function it has to be called from the math module
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)