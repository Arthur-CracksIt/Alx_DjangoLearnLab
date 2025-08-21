from django.urls import path
from .views import ListBooks, ListBooksDetail

urlpatterns = [
    path('books/', ListBooks, name= 'ListBooks')
    path('library/', ListBooksDetail.as_view(), name= 'library_details')
]