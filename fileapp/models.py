from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(models.Model):
#     username = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=255)

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True )

# from django.contrib.auth.models import CustomUser

class File(models.Model):
    file = models.FileField(upload_to='files/')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
