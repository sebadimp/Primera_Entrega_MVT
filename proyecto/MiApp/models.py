from django.db import models

class Empleados(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    fecha_alta=models.DateField()
    funcion=models.CharField(max_length=30)

class Clientes(models.Model):
    razon_social=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30)
    cuit=models.IntegerField()
    email=models.EmailField(max_length=50)

class Productos(models.Model):
    nombre_comercial=models.CharField(max_length=30)
    marca=models.CharField(max_length=30)
    droga=models.CharField(max_length=30)
    stock=models.IntegerField()
