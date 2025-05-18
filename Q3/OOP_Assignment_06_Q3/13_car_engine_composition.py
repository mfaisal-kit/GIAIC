class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
    
    def start(self):
        print(f"{self.engine_type} engine started")

class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine  # Composition - Car HAS-A Engine
    
    def start_car(self):
        print(f"Starting {self.model}")
        self.engine.start()  # Accessing Engine's method

# Create an Engine
v6_engine = Engine("V6 Turbo")

# Create a Car with the Engine (composition)
my_car = Car("Vitz", v6_engine)

# Use Car to access Engine's methods
my_car.start_car()
