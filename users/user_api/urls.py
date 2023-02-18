from django.urls import path
from .views import ListaUsuarios


urlpatterns = [
    path('user_api/', ListaUsuarios.as_view(), name='lista_usuarios'),
    
]
