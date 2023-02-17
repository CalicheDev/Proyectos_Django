from rest_framework import serializers
from .models import User

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nombre', 'email', 'telefono','password']
