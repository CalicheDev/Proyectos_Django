""" from django.shortcuts import render """

# Create your views here.
from rest_framework import generics
from rest_framework import filters
from .models import Atencion
from .serializers import AtencionSerializer

class AtencionListCreate(generics.ListCreateAPIView): #API: AtencionListCreate para crear y listar atenciones
    queryset = Atencion.objects.all()
    serializer_class = AtencionSerializer

class AtencionDetail(generics.RetrieveUpdateDestroyAPIView): #API AtencionDetail para ver, actualizar y eliminar atenciones individuales.
    queryset = Atencion.objects.all()
    serializer_class = AtencionSerializer

class AtencionList(generics.ListAPIView): #API AtencionList para ver solo las ordenes que conincidan con el numero de la formual
    serializer_class = AtencionSerializer
    queryset = Atencion.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['orden']
    
    def get_queryset(self):
        queryset = self.queryset
        orden = self.request.query_params.get('orden', None)
        if orden is not None:
            queryset = queryset.filter(orden=orden)
        return queryset
