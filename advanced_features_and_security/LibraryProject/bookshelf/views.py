from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required
from django.urls import reverse_lazy
from .models import UserPermissions
from django.views.generic import CreateView
# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@permission_required('bookshelf.can_edit', raise_exception=True)
def can_edit(request):
    edit_role= UserPermissions.objects.create(role= 'Editor')
    return render(request, 'relationship_app/editors.html', {'user': edit_role})

@permission_required('bookshelf.can_delete', raise_exception=True)
def can_delete(request):
    view_role= UserPermissions.objects.create(role= 'Viewer')
    return render(request, 'relationship_app/viewer.html', {'user': view_role})

@permission_required('bookshelf.can_view', raise_exception=True)
def can_change_book(request, name):
    delete_role = UserPermissions.objects.get(name = name)
    delete_role.delete()
    return render(request, 'templates/relationship_app/change_book.html', {'book': delete_role})

