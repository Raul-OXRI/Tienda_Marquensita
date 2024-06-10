from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path ('', views.empleado, name='empleado'),
    path ('createempleado/', views.empleadocreate, name='createempleado'),
    path ('downempleado/<int:empleado_id>/', views.eliminar_empleado, name='downempleado'),

]