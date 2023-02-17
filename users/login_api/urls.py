from django.urls import path
from .views import LoginAPIView

urlpatterns = [
    path('login_api/', LoginAPIView.as_view(), name='login_api'),
]
