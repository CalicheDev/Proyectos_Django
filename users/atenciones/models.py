from django.db import models

# Create your models here.
class Atencion(models.Model):
    fecha = models.DateField()
    fecha_atencion = models.DateField()
    documento = models.CharField(max_length=255)
    orden = models.CharField(max_length=255)
    historia = models.CharField(max_length=50)
    observaciones = models.TextField()
    tipo_novedad = models.CharField(max_length=50)
    novedad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
