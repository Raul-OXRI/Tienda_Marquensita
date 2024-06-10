from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path ('', views.cliente, name='clients'),
    
    path ('downcliente/<int:cliente_id>/', views.eliminar_cliente, name='downcliente'),
    path ('createcliente/', views.clientecreate, name='createcliente'),
    path ('clientelist/', views.clientelist, name='clientelist'),
]


