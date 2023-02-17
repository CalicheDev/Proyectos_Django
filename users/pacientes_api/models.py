# Create models for customers.
# api/models.py
from django.db import models


class Paciente(models.Model):
    fecha = models.DateField()
    mes_cita = models.CharField(max_length=255)
    documento = models.CharField(max_length=255)
    orden = models.CharField(max_length=255)
    historia = models.CharField(max_length=255)
    apellido1 = models.CharField(max_length=255)
    apellido2 = models.CharField(max_length=255)
    nombre1 = models.CharField(max_length=255)
    nombre2 = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    edad = models.IntegerField()
    telefono1 = models.CharField(max_length=20)
    telefono2 = models.CharField(max_length=20)
    direccion_residencia = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    profesional = models.CharField(max_length=255)
    profesional2 = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)
    centro_produccion = models.CharField(max_length=255)
    dosis = models.IntegerField()
    posologia = models.CharField(max_length=255)
    tratamiento = models.IntegerField()
    tiempo = models.CharField(max_length=255)

def __str__(self):
	return self.name