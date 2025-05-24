def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create instance of Person
p = Person("Farhan")

# Call the added greet() method
print(p.greet())
