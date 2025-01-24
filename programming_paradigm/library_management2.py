class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Tracks if the book is checked out

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True              

    def return_book(self):
        """Mark the book as available."""
        self._is_checked_out = False      

class Library:
    def __init__(self):
        self._books = []  # Private list to store Book objects

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)  # Ensure the book is added only once

    def check_out_book(self, title):
        """Find the book by title and check it out if available."""
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book.check_out()
                print(f"Checked out '{book.title}' successfully.")
                return
        print(f"Sorry, '{title}' is not available or already checked out.")

    def return_book(self, title):
        """Find the book by title and return it if it was checked out."""
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book.return_book()
                print(f"Returned '{book.title}' successfully.")
                return
        print(f"'{title}' was not checked out or does not exist in the library.")

    def list_available_books(self):
        """Print a list of books that are not checked out."""
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            print("\nAvailable books:")
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("\nNo books available.")