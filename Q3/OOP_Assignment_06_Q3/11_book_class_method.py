class Book:
    total_books = 0
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Increment count when a new book is created
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
    
    @classmethod
    def get_total_books(cls):
        """Class method to get the current book count"""
        return cls.total_books
    
    def display_info(self):
        """Instance method to display book info"""
        print(f"'{self.title}' by {self.author}")

# Create some books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

print(f"Current book count: {Book.get_total_books()}")  