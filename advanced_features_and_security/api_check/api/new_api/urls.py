from django.urls import path
from .views import BookApiView

urlpatterns = [
    path('api/books', BookApiView.as_view(), name = 'book_create'),
]