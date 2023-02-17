#from django.shortcuts import render

# Create your views here.
# api/views.py
from rest_framework import generics
from .models import Paciente
from .serializers import PacienteSerializer

class PacienteList(generics.ListAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
