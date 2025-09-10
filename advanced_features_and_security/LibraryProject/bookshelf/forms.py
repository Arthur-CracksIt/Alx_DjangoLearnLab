from django.contrib.auth import forms
from .models import Book

class ExampleForm(forms.UserModel):
    class Meta:
        model = Book
        fields = ['title', 'author']