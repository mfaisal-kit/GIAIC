class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute (convention)

    @property
    def price(self):
        print("Getting price...") # Getter for price
        return self._price

    @price.setter
    def price(self, new_price):
        print("Setting new price...") # Setter for price with validation

    @price.deleter
    def price(self):
        print("Deleting price...") # Deleter for price
        del self._price


# Demonstration
product = Product("Laptop", 999.99)

# Get price (using @property)
print(f"Initial price: ${product.price}")  # Calls the getter

# Set price (using @price.setter)
product.price = 899.99  # Calls the setter
print(f"Updated price: ${product.price}")

# Delete price (using @price.deleter)
del product.price  # Calls the deleter
