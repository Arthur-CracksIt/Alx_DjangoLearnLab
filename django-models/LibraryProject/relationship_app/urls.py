from django.urls import path
from .views import ListBooks, LibraryDetailView

urlpatterns = [
    path('books/', ListBooks, name= 'ListBooks')
    path('library/', LibraryDetailView.as_view(), name= 'library_details')
]