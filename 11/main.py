class Book:
    total_books = 0  # Class variable to keep track of total books

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()  # Increment count when a new book is created

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books

# Creating book instances
b1 = Book("1984")
b2 = Book("To Kill a Mockingbird")
b3 = Book("The Great Gatsby")

# Accessing the total_books count via class method
print("Total books:", Book.get_total_books())
