from django.db import models
from django.contrib.auth.models import AbstractUser

class Admin(AbstractUser):
    email = models.EmailField(unique=True)

    # Define groups and user_permissions as fields
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='admin_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='admin_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title
