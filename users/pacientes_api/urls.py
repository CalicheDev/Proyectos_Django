from django.urls import path
from .views import PacienteList

urlpatterns = [
    path('pacientes_api/', PacienteList.as_view(), name='lista_pacientes'),
]
