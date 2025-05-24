class Car:
    def __init__(self, brand):
        # Public variable
        self.brand = brand

    # Public method
    def start(self):
        print(self.brand, "car is starting...")

# Instantiate the class
my_car = Car("Toyota")

# Accessing public variable
print("Car brand:", my_car.brand)

# Accessing public method
my_car.start()
