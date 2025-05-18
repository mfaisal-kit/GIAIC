class Counter:
    # Class variable to keep track of count
    count = 0
    
    def __init__(self):
        # Increment the count when a new instance is created
        Counter.count += 1
    
    @classmethod
    def get_count(cls):
        # Class method to access the class variable
        return cls.count
    
    @classmethod
    def display_count(cls):
        # Class method to display the count
        print(f"Total objects created: {cls.get_count()}")


# Example usage
c1 = Counter()
c2 = Counter()
c3 = Counter()

Counter.display_count() 

c4 = Counter()
Counter.display_count()  