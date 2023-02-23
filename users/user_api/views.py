#from django.shortcuts import render

# Create your views here.
""" from django.http import JsonResponse
from rest_framework import permissions """
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Obtener el token de jwt
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import UsuarioSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    notes = user.note_set.all()
    serializer = UsuarioSerializer(notes, many=True)
    return Response(serializer.data)


















""" from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect """
""" La clase FormView se encuentra en el módulo django.views.generic.edit desde Django 3.1, por lo que una posible solución sería cambiar la ruta importada por: """
""" from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm

from .models import User
from .serializers import UsuarioSerializer

class ListaUsuarios(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer """
    


""" class Login(FormView):
    template_name = "login.html"
    from_class = AuthenticationForm
    success_url = reverse_lazy('user_api:lista_usuarios')
    #Decorator para proteccion de cache y navegadores
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispath(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else: 
            return super(Login,self).dispatch(request,*args,**kwargs)
    
    def form_valid(self, form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token, _ = Token.objects.get_or_create(user = user)
        if token:
            login(self.request, form.get_user())
        return super(Login, self).form_valid(form) """

    