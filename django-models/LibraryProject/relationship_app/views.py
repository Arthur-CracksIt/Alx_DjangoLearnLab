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
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import UserProfile

@login_required
def admin_view(request):
    if hasattr(request.user, 'User') and request.user.User.role == 'Admin':
        return HttpResponse("Welcome, Admin")
    return HttpResponse("Access denied.", status=403)

def librarian_view(request):
    if hasattr(request.user, 'User') and request.user.User.role == 'Librarian':
        return HttpResponse("Welcome, Libraria")
    return HttpResponse("Access denied.", status=403)

def member_view(request):
    if hasattr(request.user, 'User') and request.user.User.role == 'Member':
        return HttpResponse("Welcome, Member")
    return HttpResponse("Access denied.", status=403)