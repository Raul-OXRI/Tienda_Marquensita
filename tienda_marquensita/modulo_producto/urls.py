from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path ('', views.producto, name='products'),
    path ('crudproductos/', views.productocrud, name='crudproductos'),
]
