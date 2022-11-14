from django import forms

class CrearClienteForm(forms.Form):
    razon_social=forms.CharField()
    direccion=forms.CharField()
    cuit=forms.IntegerField()
    email=forms.EmailField()


class CrearProductosForm(forms.Form):
    nombre_comercial=forms.CharField(max_length=30)
    marca=forms.CharField(max_length=30)
    droga=forms.CharField(max_length=30)
    stock=forms.IntegerField()


class CrearEmpleadosForm(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    fecha_alta=forms.DateField()
    funcion=forms.CharField(max_length=30)



