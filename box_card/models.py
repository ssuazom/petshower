from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(verbose_name="Título",max_length=100)
    description = models.TextField(verbose_name="Descripción")
    img = models.ImageField(verbose_name="Imagen",upload_to="projects", null=True, blank=True)
    link = models.URLField(verbose_name="URL Sitio Web Admin",null=True,blank=True)
    link_user = models.URLField(verbose_name="URL Sitio Web Admin User", null=True,blank=True)
    create = models.DateTimeField(verbose_name="Fecha Creación",auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha Actualización",auto_now=True)

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-create"]

    def __str__(self):
        return self.title

class Gallery(models.Model):
    idImage = models.IntegerField(primary_key=True, verbose_name='ID')
    image_galery = models.ImageField(verbose_name="Imagen_Galeria",upload_to="projects", null=True, blank=True)
    create = models.DateTimeField(verbose_name="Fecha Creación",auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha Actualización",auto_now=True)

    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Imagenes Galeria"
        ordering = ["-create"]
