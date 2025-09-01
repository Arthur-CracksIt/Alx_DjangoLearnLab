from django.shortcuts import render
from .models import Book
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic.detail import DetailView
from .models import Library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

from django.contrib.auth import login  
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class Register(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'templates/relationship_app/register.html'
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.shortcuts import render
from .models import UserProfile

@user_passes_test
def admin_view(request):
    if hasattr(request.user, 'User') and request.user.User.role == 'Admin':
        return render(request, 'templates/relationship_app/admin_view.html')

def librarian_view(request):
    if hasattr(request.user, 'User') and request.user.User.role == 'Librarian':
       return render(request, 'templates/relationship_app/librarian_view.html')

def member_view(request):
    if hasattr(request.user, 'User') and request.user.User.role == 'Member':
       return render(request, 'templates/relationship_app/member_view.html')
    
@permission_required('templates/relationship_app.can_add_book', raise_exception=True)
def can_add_book(request):
    new_book = Book.objects.create(title = '1984', author = 'George Orwell', publication_year = 1949)
    return render(request, 'templates/relationship_app/add_book.html', {'book': new_book})

@permission_required('templates/relationship_app.can_change_book', raise_exception=True)
def can_change_book(request, title):
    new_book = Book.objects.get(title = title)
    return render(request, 'templates/relationship_app/change_book.html', {'book': new_book})

@permission_required('templates/relationship_app.can_delete_book', raise_exception=True)
def can_change_book(request, title):
    new_book = Book.objects.get(title = title)
    new_book.delete()
    return render(request, 'templates/relationship_app/change_book.html', {'book': new_book})