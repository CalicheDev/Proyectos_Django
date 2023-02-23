""" from django.shortcuts import render """

# Create your views here.
from rest_framework import generics
from .models import Atencion
from .serializers import AtencionSerializer

class AtencionListCreate(generics.ListCreateAPIView): #API: AtencionListCreate para crear y listar atenciones
    queryset = Atencion.objects.all()
    serializer_class = AtencionSerializer

class AtencionDetail(generics.RetrieveUpdateDestroyAPIView): #API AtencionDetail para ver, actualizar y eliminar atenciones individuales.
    queryset = Atencion.objects.all()
    serializer_class = AtencionSerializer
