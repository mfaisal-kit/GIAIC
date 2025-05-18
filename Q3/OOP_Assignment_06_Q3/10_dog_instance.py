class Dog:
    def __init__(self, name, breed):
        self.name = name    # Instance variable
        self.breed = breed  # Instance variable
    
    def bark(self):
        print(f"{self.name} the {self.breed} says: Woof!")


# Create Dog instances
dog1 = Dog("Tomy", "Golden Retriever")
dog2 = Dog("Bella", "Beagle")

# Call the bark method
dog1.bark()  
dog2.bark()  
