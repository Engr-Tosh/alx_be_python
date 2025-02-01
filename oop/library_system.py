#Deepening my understanding of inheritance and composition in Python by creating a system that models a library with different types of books.

#Creating the base class books
class Book:
    def __init__(self, title, author):
        self.title = str(title)
        self.author = str(author)

#Creating the inherited/derived classes

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = int(file_size)
        
        
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = int(page_count)

#Creating class to demonstrate composition
class Library:
    def __init__(self):

        self.books = []     #A list to store te instances of Book, EBook and Printbook

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print(self.books)