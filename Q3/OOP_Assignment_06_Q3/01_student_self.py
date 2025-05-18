class Student:
    def __init__(self, name, marks):
        # Initialize instance variables using self
        self.name = name
        self.marks = marks
    
    def display(self):
        # Method to display student details
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")


# Example usage
student1 = Student("Ali", 97)
student1.display()

student2 = Student("Ibrahim", 89)
student2.display()