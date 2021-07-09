from django.db import models

# Create your models here.

class Veterinarios(models.Model):
    idVeterinario = models.IntegerField(primary_key=True, verbose_name='ID')
    nombre = models.CharField(verbose_name='Nombre',max_length=50)
    descripcion = models.TextField(verbose_name='Descripción')
    image_veterinario = models.ImageField(verbose_name='Imagen', upload_to='projects', null=True,blank=True)
    link_facebook = models.URLField(verbose_name='URL Link Facebook',null=True,blank=True)
    link_instagram = models.URLField(verbose_name='URL Link Instagram',null=True,blank=True)
    link_whatsapp = models.URLField(verbose_name='URL Link Whatsapp',null=True,blank=True)
    link_twitter = models.URLField(verbose_name='URL Link Twitter',null=True,blank=True)
    create = models.DateTimeField(verbose_name='Fecha Creación',auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Fecha Actualización',auto_now=True)

    class Meta:
        verbose_name='Veterinario Socio'
        verbose_name_plural='Veterinarios Socios'
        ordering = ['idVeterinario']
    
    def __str__(self):
        return self.nombre
