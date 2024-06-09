from django import forms 
from .models import Cliente


class ClienteForm(forms.ModelForm):
    from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre_client', 
            'apellido_client', 
            'correo_client', 
            'telefono_client', 
            'direccion_client', 
            'password', 
            'estado'
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }
