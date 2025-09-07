from django.contrib import admin
from .models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin): #customizing the admin
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'publication_year')
admin.site.register(Book, BookAdmin)