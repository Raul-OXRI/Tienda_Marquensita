from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_client', 'apellido_client', 'correo_client', 'telefono_client',
        'direccion_client', 'fecha_registro_client', 'estado'
    )

admin.site.register(Cliente, ClienteAdmin)
