from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Producto
from .forms import ProductoForm

# Create your views here.

def producto(request):
    return render(request, 'producto.html')

def productocrud(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')  
    else:
        form = ProductoForm()
    
    productos = Producto.objects.filter(estado='1')  # Assuming '1' is the string for the active state
    return render(request, "crud_productos.html", {'form': form, 'productos': productos})

def eliminar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id=id_producto)
    producto.estado = '0'  # Assuming '0' is the string for the inactive state
    producto.save()
    return redirect('products')
