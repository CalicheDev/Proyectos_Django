# Create your models here.
from django.db import models

class User(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

def __str__(self):
	return self.name

