# Generated by Django 4.1.3 on 2022-11-14 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('cuit', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('fecha_alta', models.DateField()),
                ('funcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comercial', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('droga', models.CharField(max_length=30)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
