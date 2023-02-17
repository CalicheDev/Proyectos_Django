from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.conf import settings
from datetime import datetime, timedelta
import jwt
from .serializers import UserSerializer

class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is None:
            return Response({'error': 'Credenciales invalidas'}, status=status.HTTP_401_UNAUTHORIZED)

        # Generar un token de acceso para el usuario
        access_token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(days=1)
        }, settings.SECRET_KEY, algorithm='HS256')

        # Actualizar el campo access_token del usuario
        user.access_token = access_token
        user.save()

        # Enviar la respuesta con los datos del usuario y el token de acceso
        serializer = UserSerializer(user)
        return Response(serializer.data)
