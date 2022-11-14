from django.shortcuts import render
from .models import Empleados,Clientes,Productos
from .forms import CrearClienteForm,CrearProductosForm,CrearEmpleadosForm


def mostrar_index(request):

    return render(request,'index.html')


def acerca_de_mi(request):

    return render(request,"acerca_de_mi.html")

def crear_cliente(request):

    if request.method=="POST":

        formulario=CrearClienteForm(request.POST)

        if formulario.is_valid():

            formulario_limpio=formulario.cleaned_data

            cliente=Clientes(razon_social=formulario_limpio['razon_social'],direccion=formulario_limpio['direccion'],cuit=formulario_limpio['cuit'],email=formulario_limpio['email'])

            cliente.save()

            return render(request,'index.html') #redirecciona a la pagina principal

    else:

        formulario=CrearClienteForm()

    return render(request,'crear_cliente.html',{'formulario':formulario})


def crear_producto(request):

    if request.method=="POST":

        formulario=CrearProductosForm(request.POST)

        if formulario.is_valid():

            formulario_limpio=formulario.cleaned_data

            producto=Productos(nombre_comercial=formulario_limpio['nombre_comercial'],marca=formulario_limpio['marca'],droga=formulario_limpio['droga'],stock=formulario_limpio['stock'])

            producto.save()

            return render(request,'index.html') #redirecciona a la pagina principal

    else:
        formulario=CrearProductosForm()

    return render(request,'crear_producto.html',{'formulario':formulario})


def buscar_producto(request):

    if request.GET.get('droga',False):
        droga=request.GET['droga']
        productos=Productos.objects.filter(droga__icontains=droga)

        return render(request,'buscar_producto.html',{'productos':productos})

    else:
        respuesta="No hay datos"

    return render(request,'buscar_producto.html',{'respuesta':respuesta})


def crear_empleado(request):

    if request.method=="POST":

        formulario=CrearEmpleadosForm(request.POST)

        if formulario.is_valid():

            formulario_limpio=formulario.cleaned_data

            empleado=Empleados(nombre=formulario_limpio['nombre'],apellido=formulario_limpio['apellido'],fecha_alta=formulario_limpio['fecha_alta'],funcion=formulario_limpio['funcion'])

            empleado.save()

            return render(request,'index.html') #redirecciona a la pagina principal

    else:
        formulario=CrearEmpleadosForm()

    return render(request,'crear_empleados.html',{'formulario':formulario})