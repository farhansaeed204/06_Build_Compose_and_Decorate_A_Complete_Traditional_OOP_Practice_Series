# Define custom exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. Age must be 18 or older.")
    else:
        print(f"Age {age} is valid.")

# Test with try-except
try:
    check_age(16)
except InvalidAgeError as e:
    print("Caught an exception:", e)

try:
    check_age(21)
except InvalidAgeError as e:
    print("Caught an exception:", e)
