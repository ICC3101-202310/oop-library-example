from book import Book
from library import Library

book_1 = Book('Enciclopedia', 'Desconocido')
print(book_1)
print(book_1.name)
book_2 = Book('Eloquent Javascript', 'John Doe')
print(book_2.name)

my_library = Library()
print(my_library.books)
my_library.add_new_book(book_1)
my_library.add_new_book(book_2)
# print(my_library.books)
# for book in my_library.books:
#     print(book)
my_library.show_books()