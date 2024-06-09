from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True,)
    nombre_client = models.CharField(max_length=100, null=True, blank=True)
    apellido_client = models.CharField(max_length=100, null=True, blank=True)
    correo_client = models.CharField(max_length=50, null=True, blank=True)
    telefono_client = models.CharField(max_length=13, null=True, blank=True)
    direccion_client = models.CharField(max_length=50, null=True, blank=True)
    fecha_registro_client = models.DateTimeField(auto_now_add=True, )  
    password = models.CharField(max_length=128)
    estado = models.CharField(max_length=50, null=True, blank=True)
    

    def save(self, *args, **kwargs):
        if not self.pk or Cliente.objects.get(pk=self.pk).password != self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    #def save(self, *args, **kwargs):
    #    self.password = make_password(self.password)
    #    super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre_client}{self.apellido_client}" if self.nombre_client else "Unnamed Client"