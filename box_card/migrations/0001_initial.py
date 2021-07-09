# Generated by Django 3.2.5 on 2021-07-08 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('idImage', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('image_galery', models.ImageField(blank=True, null=True, upload_to='projects', verbose_name='Imagen_Galeria')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha Actualización')),
            ],
            options={
                'verbose_name': 'Galeria',
                'verbose_name_plural': 'Imagenes Galeria',
                'ordering': ['-create'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('img', models.ImageField(blank=True, null=True, upload_to='projects', verbose_name='Imagen')),
                ('link', models.URLField(blank=True, null=True, verbose_name='URL Sitio Web')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha Actualización')),
            ],
            options={
                'verbose_name': 'proyecto',
                'verbose_name_plural': 'proyectos',
                'ordering': ['-create'],
            },
        ),
    ]