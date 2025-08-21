from django.urls import path
from .views import ListBooks

urlpatterns = [
    path('books/', ListBooks, name= 'ListBooks')
]