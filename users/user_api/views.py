#from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import User
from .serializers import UsuarioSerializer

class ListaUsuarios(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    
