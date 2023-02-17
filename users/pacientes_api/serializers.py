from rest_framework import serializers
from .models import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = [ 'id', 'fecha', 'mes_cita', 'documento', 'orden', 'historia', 'apellido1', 'apellido2', 'nombre1', 'nombre2', 'empresa', 'edad', 'telefono1', 'telefono2', 
        'direccion_residencia', 'codigo', 'descripcion', 'cantidad', 'profesional', 'profesional2', 'especialidad', 'centro_produccion', 'dosis', 'posologia', 'tratamiento', 'tiempo']