from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from main.manager import UserManager 
# Create your models here.



class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Personal Info
    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(max_length=100, null=True, blank=True)
    
    # Verification
    is_verified = models.BooleanField(default=False)

    # DateTime
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.is_verified = True
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.email



class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False)


    def save(self, *args, **kwargs):
        self.id = self.user.id
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.user.email
