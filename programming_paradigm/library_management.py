#The objective of this project is to solidify my understanding of basic oop concepts in python by implementing a system that tracks books in a library, focusing on classes, object instantiation, and method invocation.

#Implement a book class and methods to check a book and return it
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False   #Track if the book is checked'''
           
    def check_out(self):
        self._is_checked_out = True   #'''Marks the book as checked therefore not available'''           

    def return_book(self):
        self._is_checked_out = False      #'''Marks the book as available'''
    

class Library:
    '''using a variable to store instances of book'''

    def __init__(self):
        self._books = []       #Private list to store Book objects

    def add_book(self, book):
        self._books.append(book)      #Ensures that the book is added only once
        
    def check_out_book(self, title):
        '''Find the book by title'''
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book.check_out()
                return
            

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book.return_book()
                return

    def list_available_books(self):
        #list of books that are not checked out
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available")