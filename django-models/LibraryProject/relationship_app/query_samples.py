from relationship_app.models import Book, Library, Author, Librarian
#Get all books
book = Book.objects.all()

#Get books in library
library_name = "Balm Library"
library = Library.objects.get(name=library_name)
books = library.books.all()
print(f"Books in {library_name}:" )
for book in books:
    print(book.title)

#Get book by author
author_name = 'David'
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
print(f"Books by {author_name}:", list(books))

#Get Librarian for a Library
librarian_name = 'Kofi'
librarian = Librarian.objects.get(name = librarian_name)
library = librarian.library.all()
print(f"Library for {librarian_name}:" )
for lib in library:
    print(lib.name)