from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    crimesection_admin = models.BooleanField(default=False)
    entertainment_admin = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['crimesection_admin', 'entertainment_admin', 'phone']

    def __str__(self):
        return self.username




