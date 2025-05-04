# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0  
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
    
    @classmethod
    def get_total_books(cls):
        return cls.total_books

# Test
b1 = Book("To Kill a Mockingbird", "Harper Lee")
b2 = Book("Harry Potter", "J.K. Rowling")
print(Book.get_total_books())  # Output: 2




