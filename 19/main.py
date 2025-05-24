class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

# Create an instance of Multiplier
double = Multiplier(2)

# Check if the object is callable
print("Is 'double' callable?", callable(double))

# Call the object like a function
result = double(5)
print("Result of double(5):", result)
