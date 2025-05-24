class Student:
    def __init__(self, name, marks):
        # Initialize instance variables using self
        self.name = name
        self.marks = marks

    def display(self):
        # Display student details
        print("Student Name:", self.name)
        print("Marks:", self.marks)

# Example usage
student1 = Student("Farhan", 88)
student1.display()
