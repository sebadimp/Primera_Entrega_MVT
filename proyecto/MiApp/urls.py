"""tp_mvt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import mostrar_index,acerca_de_mi,crear_cliente,crear_producto,buscar_producto,crear_empleado

urlpatterns = [
    path('', mostrar_index,name='principal'),
    path('acerca_de_mi/',acerca_de_mi, name='acerca de mi'),
    path('crear_cliente/',crear_cliente, name='crear cliente'),
    path('crear_producto/',crear_producto, name='crear producto'),
    path('buscar_producto/',buscar_producto, name='buscar producto'),
    path('crear_empleados/',crear_empleado, name='crear empleado')
] 