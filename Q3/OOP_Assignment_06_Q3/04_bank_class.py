class Bank:
    # Class variable
    bank_name = "National Trust Bank"
    
    def __init__(self, branch):
        self.branch = branch  # Instance variable
    
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
    
    def display_info(self):
        print(f"{Bank.bank_name} - {self.branch} branch")

# Create instances
bank1 = Bank("Malir")
bank2 = Bank("Korangi")

print("Initial state:")
bank1.display_info() 
bank2.display_info()  

# Change bank name using class method
Bank.change_bank_name("Standard Bank")

# Show updated state
print("\nAfter name change:")
bank1.display_info() 
bank2.display_info() 
