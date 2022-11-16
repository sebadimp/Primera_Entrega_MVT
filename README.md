# Primera_Entrega_MVT

por Sebastian D'Imperio.

Esta es una instancia de evaluación para el curso Python de Coderhouse. Consta de :
- Herencias de plantillas 
- 3 clases de modelos
- un formulario para ingresar datos a las 3 clases
- un formulario para buscar algo en la BD

# Cómo instalar y ejecutar el proyecto

Se debe crear el entorno virtual de python:

-python -m venv venv

Luego activamos el entorno con el siguiente comando:

-source venv\Scripts\activate

Luego procedemos a instalar Django:

-pip install Django

Iniciamos nuestro proyecto.


-cd proyecto

-python manage.py runserver

# Descripción
Para encarar el proyecto, me base en el modelo de negocio de una Droguería, un rubro en el cual trabaje hace 10 años. Este tipo de empresas se encargan de comprar y vender medicamentos entre otros productos.

Cuenta con tres modelos:
1) Empleados
2) Clientes
3) Productos

En cada uno de ellos, se puede guardar registros en la BD.

Dentro del apartado de Productos, hay una etiqueta que referencia a la búsqueda de los mismos, la cual tiene como filtro el tipo de "droga".
Ej.

-Nombre comercial: Tafirol

-Droga: Paracetamol.

Un acerca de mi, el cual realiza herencia de plantillas, mostrando una breve descripción para demostrar su funcionamiento.


# Observaciones

Es un primer acercamiento al proyecto final del Blog.
