from django.contrib import admin
from .models import Empleado

# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_empleado',
        'apellido_empleado', 
        'correo_empleado', 
        'fecha_registro_empleado'
    )

admin.site.register(Empleado, EmpleadoAdmin)