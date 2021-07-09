# Generated by Django 3.2.5 on 2021-07-08 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veterinarios',
            fields=[
                ('idVeterinario', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('image_veterinario', models.ImageField(blank=True, null=True, upload_to='projects', verbose_name='Imagen')),
                ('link_facebook', models.URLField(blank=True, null=True, verbose_name='URL Link Facebook')),
                ('link_instagram', models.URLField(blank=True, null=True, verbose_name='URL Link Instagram')),
                ('link_whatsapp', models.URLField(blank=True, null=True, verbose_name='URL Link Whatsapp')),
                ('link_twitter', models.URLField(blank=True, null=True, verbose_name='URL Link Twitter')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha Actualización')),
            ],
            options={
                'verbose_name': 'Veterinario Socio',
                'verbose_name_plural': 'Veterinarios Socios',
                'ordering': ['idVeterinario'],
            },
        ),
    ]