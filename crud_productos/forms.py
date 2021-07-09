from django import forms
from django.forms import ModelForm
from .models import Producto

class Productoform(ModelForm):

    class Meta:
        model = Producto
        fields = [
            'idProducto',
            'nombre',
            'descripcion',
            'image_producto',
            'precio',
            'stock',
            'marca',
        ]
        labels = {
            'idProducto': 'Codigo Producto',
            'nombre': 'Nombre Producto',
            'descripcion': 'Descripcion',
            'image_producto': 'Imagen',
            'precio': 'Precio Unitario',
            'stock': 'Stock',
            'marca': 'Marca',
        }
        widgets = {
            'idProducto' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Codigo Producto'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre Producto'}),
            'descripcion' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Descripcion'}),
            'image_producto' : forms.FileInput(attrs={'class':'form-control'}),
            'precio' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Precio Unitario'}),
            'stock' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Stock'}),
            'marca' : forms.Select(attrs={'class':'form-control', 'placeholder': 'Marca'}),
        }