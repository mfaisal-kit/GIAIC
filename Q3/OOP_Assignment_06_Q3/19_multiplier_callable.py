class Multiplier:
    def __init__(self, factor):
        self.factor = factor # Initialize with a multiplication factor
    
    def __call__(self, x):
        return x * self.factor # Make instances callable - multiply input by factor


# Create a multiplier object
double = Multiplier(2)
triple = Multiplier(3)

# Test if objects are callable
print("Is double callable?", callable(double))  # True
print("Is triple callable?", callable(triple))  # True

# Call objects like functions
print("Double of 5:", double(5))    # 10 (2 * 5)
print("Triple of 5:", triple(5))    # 15 (3 * 5)
print("Double of 3.5:", double(3.5))  # 7.0 (2 * 3.5)

# Can still access the factor attribute
print("Multiplication factor:", double.factor)  # 2