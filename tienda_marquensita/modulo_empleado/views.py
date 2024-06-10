from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.


def empleado (request):
    return render(request, 'crudempleado.html')

def empleadocreate(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.estado = '1' 
            form.save()
            return redirect('empleado')
    else:
        form = EmpleadoForm()

    empleados = Empleado.objects.filter(estado='1')
    return render(request, "formsEmpleado.html", {'form': form, 'empleados': empleados})

def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, empleado_id=empleado_id)
    empleado.estado = '0'
    empleado.save()
    return redirect('empleadolist')
