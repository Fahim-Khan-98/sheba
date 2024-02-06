from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, crimesection_admin, entertainment_admin, phone, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')

        user = self.model(
            username=username,
            crimesection_admin=crimesection_admin,
            entertainment_admin=entertainment_admin,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, crimesection_admin, entertainment_admin, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, crimesection_admin, entertainment_admin, phone, password, **extra_fields)

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




