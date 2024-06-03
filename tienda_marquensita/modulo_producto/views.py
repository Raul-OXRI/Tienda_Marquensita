from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Producto
from .forms import ProductoForm
# Create your views here.

def producto(request):
    return render(request, 'producto.html')

def productocrud(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')  
    else:
        form = ProductoForm()
    
    productos = Producto.objects.filter(estado=1)  # Obtener todos los productos
    return render(request, "crud_productos.html", {'form': form, 'productos': productos})

def delete_product(request, product_id):
    producto = get_object_or_404(Producto, id=product_id)
    producto.estado = 0
    producto.save()
    return redirect('products')