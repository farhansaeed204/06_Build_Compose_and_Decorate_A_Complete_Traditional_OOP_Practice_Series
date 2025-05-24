class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP is starting...")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Composition: Engine object passed here

    def start_car(self):
        print(f"{self.brand} car is ready to go.")
        self.engine.start()  # Accessing Engine's method via Car

# Create an Engine object
engine1 = Engine(250)

# Pass Engine object to Car object
my_car = Car("Toyota", engine1)

# Start the car which starts the engine
my_car.start_car()
