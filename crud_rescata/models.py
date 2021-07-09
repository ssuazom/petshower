from django.db import models

# Create your models here.
#
# class Tipo(models.Model):
#     idTipo = models.IntegerField(primary_key=True, verbose_name='ID')
#     tipo = models.CharField(max_length=50, verbose_name='Tipo')

#     class Meta:
#         verbose_name = 'tipo'
#         verbose_name_plural = 'tipos'
#         ordering = ['tipo']
    
#     def __str__(self):
#         return self.tipo


class Mascota(models.Model):
    idMascota = models.CharField(primary_key=True, max_length=10, verbose_name='ID')
    nombre = models.CharField(max_length=50, verbose_name='Nombre Mascota')
    image_mascota = models.ImageField(verbose_name='Imagen', upload_to='projects', null=True,blank=True)
    edad = models.IntegerField(verbose_name='Edad')
    tipo = models.CharField(max_length=50, verbose_name='Tipo')
    create = models.DateTimeField(verbose_name='Fecha Creación',auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Fecha Actualización',auto_now=True)

    class Meta:
        verbose_name = 'mascota'
        verbose_name_plural = 'mascotas'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
