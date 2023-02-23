# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

def __str__(self):
	return self.name

