from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path ('', views.producto, name='products'),
    path ('crudproductos/', views.productocrud, name='crudproductos'),
    path ('donwproducto/<int:id>/', views.eliminar_producto, name='downproducto')
]
