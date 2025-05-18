class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")


class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: reference to existing Employee object

    def display_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.display_info()


# Create an Employee object independently
emp1 = Employee(101, "Ali Raza")

# Create a Department object that references the existing Employee
dept1 = Department("IT", emp1)

# Display info
dept1.display_details()
