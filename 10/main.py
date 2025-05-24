class Dog:
    def __init__(self, name, breed):
        self.name = name     # Instance variable
        self.breed = breed   # Instance variable

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

# Creating an instance of Dog
dog1 = Dog("Buddy", "Golden Retriever")

# Calling the instance method
dog1.bark()
