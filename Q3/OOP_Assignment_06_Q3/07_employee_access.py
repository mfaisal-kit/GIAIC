class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public variable
        self._salary = salary   # Protected variable (single underscore)
        self.__ssn = ssn       # Private variable (double underscore)

    def display_info(self):
        """Method to display all employee info (including protected/private)"""
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")


# Create an Employee object
emp = Employee("Ahmed", 80000, "123-45-6789")

# Accessing variables from outside the class
print("=== Accessing variables directly ===")
print("Public name:", emp.name)           # Works fine
print("Protected _salary:", emp._salary) # Works but convention says don't do this
