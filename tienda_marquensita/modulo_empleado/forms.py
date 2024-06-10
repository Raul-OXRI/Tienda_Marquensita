from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirmar contraseña')
    
    class Meta:
        model = Empleado
        fields = [
            'nombre_empleado', 
            'apellido_empleado', 
            'correo_empleado', 
            'password', 
        ]
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                self.add_error('confirm_password', 'Las contraseñas no coinciden')
        
        return cleaned_data