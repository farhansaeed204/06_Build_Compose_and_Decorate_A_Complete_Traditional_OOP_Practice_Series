class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor called")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call base class constructor
        self.subject = subject
        print("Teacher constructor called")

    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)

# Create a Teacher object
t = Teacher("Farhan", "Mathematics")
t.display()
