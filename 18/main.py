class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        print("Getting price")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        print("Setting price")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price")
        del self._price

# Using the Product class
p = Product(100)

# Access the price (calls getter)
print(p.price)

# Update the price (calls setter)
p.price = 150
print(p.price)

# Delete the price (calls deleter)
del p.price

# Trying to access after deletion will raise an AttributeError
# print(p.price)  # Uncommenting this line will raise an error
