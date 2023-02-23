from django.urls import path
from .views import AtencionListCreate, AtencionDetail

urlpatterns = [    
    path('atenciones/', AtencionListCreate.as_view(), name='atencion_list_create'),
    path('atenciones/<int:pk>/', AtencionDetail.as_view(), name='atencion_detail'), #<int:pk>/ para indicar que la URL incluirá un parámetro de tipo entero
]
