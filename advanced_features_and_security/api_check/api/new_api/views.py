from django.shortcuts import render
from rest_framework import generics
from .serializer import BookSerializer
from .models import Book

# Create your views here.
class BookApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
