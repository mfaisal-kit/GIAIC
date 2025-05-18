class Car:
    # Constructor with public variable
    def __init__(self, brand):
        self.brand = brand  # Public variable
    
    # Public method
    def start(self):
        print(f"{self.brand} car started!")

my_car = Car("Toyota")

# Accessing public variable from outside the class
print("Car brand:", my_car.brand) 

# Calling public method from outside the class
my_car.start()

# Modifying public variable from outside the class
my_car.brand = "Honda"
my_car.start()  