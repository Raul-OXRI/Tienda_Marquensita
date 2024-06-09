from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Cliente
from .forms import ClienteForm

# Create your views here.

def cliente(request):
    return render(request, 'accessportal.html')

def clientecrud(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients')
    else:
        form = ClienteForm()

    clientes = Cliente.objects.filter(estado='1')
    return render(request, "form.html", {'form': form})

def eliminar_cliente(request, producto_id):
    producto = get_object_or_404(Cliente, producto_id=producto_id)
    producto.estado = '0'  # Assuming '0' is the string for the inactive state
    producto.save()
    return redirect('clients')