from relationship_app.models import Book, Library
book = Book.objects.all()
library_name = "Balm Library"
library = Library.objects.get(name='library_name')
books = library.books.all()
print(f"Books in {library_name}:" )
for book in books:
    print(book.title)