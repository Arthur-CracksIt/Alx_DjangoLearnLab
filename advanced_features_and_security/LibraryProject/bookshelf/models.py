from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200 )
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return super().__str__()
class CustomUserManager(BaseUserManager):
    def create_user():
        new_user = CustomUser.objects.create()
        return new_user
    def create_superuser():
        super_user = CustomUser.objects.create()
        return super_user

class UserPermissions(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name
    
    class Meta:
        permissions = [
            ('Can_edit', 'can_create', 'can_edit'),
            ('can_view', 'Can_view'),
            ('Can_delete', 'can_delete'),
        ]