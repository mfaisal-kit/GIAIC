class Person:
    def __init__(self, name):
        """Base class constructor"""
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        """Derived class constructor"""
        super().__init__(name)  # Call base class constructor
        self.subject = subject  # Add Teacher-specific attribute

print("\nCreating Teacher:")
teacher = Teacher("Ahmed", "Mathematics")
print(teacher.name, teacher.subject) 