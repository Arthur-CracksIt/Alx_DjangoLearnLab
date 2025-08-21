from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('books/',list_books, name= 'ListBooks'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name= 'library_details'),
    path('login/', LoginView.as_view(template_name = 'template/relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]