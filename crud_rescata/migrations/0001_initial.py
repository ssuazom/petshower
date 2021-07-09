# Generated by Django 3.2.5 on 2021-07-08 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('idTipo', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50, verbose_name='Marca')),
            ],
            options={
                'verbose_name': 'tipo',
                'verbose_name_plural': 'tipos',
                'ordering': ['tipo'],
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('idMascota', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre Mascota')),
                ('image_mascota', models.ImageField(blank=True, null=True, upload_to='projects', verbose_name='Imagen')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha Actualización')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_rescata.tipo')),
            ],
            options={
                'verbose_name': 'mascota',
                'verbose_name_plural': 'mascotas',
                'ordering': ['nombre'],
            },
        ),
    ]
