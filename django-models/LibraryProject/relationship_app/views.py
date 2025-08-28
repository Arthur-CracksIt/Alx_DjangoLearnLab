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
from django.contrib.auth.decorators import user_passes_test
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