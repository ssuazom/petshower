from django.db import models

# Create your models here.
class Marca(models.Model):
    idMarca = models.IntegerField(primary_key=True, verbose_name='ID')
    marca = models.CharField(max_length=50, verbose_name='Marca')

    class Meta:
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'
        ordering = ['marca']
    
    def __str__(self):
        return self.marca


class Producto(models.Model):
    idProducto = models.CharField(primary_key=True, max_length=10, verbose_name='ID')
    nombre = models.CharField(verbose_name='Nombre',max_length=50)
    descripcion = models.CharField(max_length=100, verbose_name='Descripción')
    image_producto = models.ImageField(verbose_name='Imagen', upload_to='projects', null=True,blank=True)
    precio = models.IntegerField(verbose_name='Precio Unitario')
    stock = models.IntegerField(verbose_name='Stock')
    marca = models.ForeignKey(Marca, on_delete = models.CASCADE)
    create = models.DateTimeField(verbose_name='Fecha Creación',auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Fecha Actualización',auto_now=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['idProducto']
    
    def __str__(self):
        return self.idProducto
