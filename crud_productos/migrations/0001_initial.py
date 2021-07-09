# Generated by Django 3.2.5 on 2021-07-08 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('idMarca', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
            ],
            options={
                'verbose_name': 'marca',
                'verbose_name_plural': 'marcas',
                'ordering': ['marca'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
                ('image_producto', models.ImageField(blank=True, null=True, upload_to='projects', verbose_name='Imagen')),
                ('precio', models.IntegerField(verbose_name='Precio Unitario')),
                ('stock', models.IntegerField(verbose_name='Stock')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha Actualización')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_productos.marca')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['idProducto'],
            },
        ),
    ]