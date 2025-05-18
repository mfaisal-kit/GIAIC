class Logger:
    def __init__(self, name):
        """Constructor - called when object is created"""
        self.name = name
        print(f"Logger '{self.name}' created")

    def __del__(self):
        """Destructor - called when object is about to be destroyed"""
        print(f"Logger '{self.name}' destroyed")

    def log(self, message):
        """Regular instance method"""
        print(f"[{self.name}] {message}")


# Demonstration
print("Starting program...")

# Create an object (constructor called)
logger1 = Logger("System")
logger1.log("Initializing components...")

# Create another object
logger2 = Logger("Network")
logger2.log("Establishing connection...")

# Explicitly delete an object
print("\nDeleting logger2...")
del logger2

print("\nProgram continuing...")
logger1.log("Operation complete")

# logger1 will be automatically deleted when program ends
print("\nEnd of program - objects will be destroyed")