from relationship_app.models import Book, Library
book = Book.objects.all()
library = Library.objects.get(name='library_name')
