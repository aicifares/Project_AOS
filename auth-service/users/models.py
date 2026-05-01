from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom user model extending Django's AbstractUser
class User(AbstractUser):
    
    # Role choices
    ROLE_CHOICES = (
        ('CLIENT', 'Client'),
        ('ADMIN', 'Admin'),
    )

    # New field
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='CLIENT')
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username