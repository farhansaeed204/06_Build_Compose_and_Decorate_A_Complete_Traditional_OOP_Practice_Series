class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display(self):
        print(f"Employee: {self.name}, Position: {self.position}")

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee  # Aggregation: reference to an Employee object

    def show_department(self):
        print(f"Department: {self.name}")
        self.employee.display()

# Creating Employee object independently
emp1 = Employee("Farhan", "Software Engineer")

# Passing existing Employee object to Department
dept = Department("IT", emp1)

# Display details
dept.show_department()

# Employee still exists independently
emp1.display()
