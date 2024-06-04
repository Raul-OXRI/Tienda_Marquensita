from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre_producto', 
            'descripcion_producto', 
            'precio_producto', 
            'stock_producto', 
            'imagen_producto',
        ]

    estado = forms.CharField(max_length=50, initial='1', required=False)

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['estado'].initial = '1'
        


        