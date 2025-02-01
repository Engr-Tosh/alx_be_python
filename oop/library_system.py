#Deepening my understanding of inheritance and composition in Python by creating a system that models a library with different types of books.

#Creating the base class books
class Book:
    def __init__(self, title, author):
        self.title = str(title)
        self.author = str(author)

    def __str__(self):
        return f"Book: {self.title} by {self.author}"
        

#Creating the inherited/derived classes

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = int(file_size)

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
        
        
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = int(page_count)

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

#Creating class to demonstrate composition
class Library:
    def __init__(self):    
        #A list to store te instances of Book, EBook and Printbook
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)     #This calls the __str__ method of each class properly