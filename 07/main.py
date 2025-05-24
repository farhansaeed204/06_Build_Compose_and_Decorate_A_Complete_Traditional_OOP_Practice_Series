class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # Public variable
        self._salary = salary    # Protected variable (convention)
        self.__ssn = ssn         # Private variable (name mangling)

    def display(self):
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN (accessed within class):", self.__ssn)

# Creating an object
emp = Employee("Farhan", 50000, "123-45-6789")

# Accessing variables
print("Accessing public variable:", emp.name)         # ✅ Works
print("Accessing protected variable:", emp._salary)   # ⚠️ Works, but not recommended
# print("Accessing private variable:", emp.__ssn)      # ❌ Error: AttributeError

# Correct way to access private variable (if needed)
print("Accessing private variable (using name mangling):", emp._Employee__ssn)

# Accessing all from a method inside the class
emp.display()
