from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    def __str__(self):
        return self.title
    
    class Meta:
        permissions = [
            ('Can_add_book', 'can_add_book'),
            ('can_change_book', 'Can_change_book'),
            ('Can_delete_book', 'can_delete_book')
        ]
    
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='library')
    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length = 200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='User')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user = instance)

from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    user = models.OneToOneField(AbstractUser, models.CASCADE, related_name='CustomUser')
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

    def __str__(self):
        return super().__str__()