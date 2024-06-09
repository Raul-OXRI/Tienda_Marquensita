from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path ('', views.cliente, name='clients'),
    path ('crudclientes/', views.clientecrud, name='crudclientes'),
    #path ('downcliente/<int:cliente_id>/', views.eliminar_cliente, name='downcliente')
    path ('createcliente/', views.clientecrud, name='createcliente'),
]


