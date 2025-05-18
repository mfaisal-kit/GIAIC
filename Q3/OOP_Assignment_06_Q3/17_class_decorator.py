def add_greeting(cls):
    def greet(self): # Class decorator definition
        return "Hello from Decorator!"
    
    # Add the new method to the class
    cls.greet = greet
    return cls

# Apply the decorator to a class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Test the decorated class
p = Person("Ali Raza")
print(p.greet())  
print(p.name)     