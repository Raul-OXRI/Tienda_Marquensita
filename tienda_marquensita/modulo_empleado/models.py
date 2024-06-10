from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.


class Empleado(models.Model):
    empleado_id = models.AutoField(primary_key=True,)
    nombre_empleado = models.CharField(max_length=50, null=True, blank=True)
    apellido_empleado = models.CharField(max_length=50, null=True, blank=True)
    correo_empleado = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=150)
    fecha_registro_empleado = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='1')

    def save (self, *args, **kwargs):
        if not self.pk or Empleado.objects.get(pk=self.pk).password != self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.nombre_empleado}{self.apellido_empleado}" if self.nombre_empleado else "Unnamed Employee"

