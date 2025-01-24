#The objective of this project is to solidify my understanding of basic oop concepts in python by implementing a system that tracks books in a library, focusing on classes, object instantiation, and method invocation.

#Implement a book class and methods to check a book and return it
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = bool
           
    def check_out(self):
        self._is_checked_out = True              

    def return_book(self):
        self._is_checked_out = False      
    

class Library:
    '''using a variable to store instances of book'''

    def __init__(self):
        self._books = []       #Private list to store Book objects

    def add_book(self, book):
        self._books.append(book)
        
    def check_out_book(self, title):
        self._books.remove(title)

    def return_book(self, title):
        self._books.append(title)

    def list_available_books(self):
        return self._books