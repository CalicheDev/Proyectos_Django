from django.contrib import admin
from .models import Atencion
# Register your models here.
@admin.register(Atencion)
class AtencionAdmin(admin.ModelAdmin):
    pass