from django import forms
from django.forms import ModelForm
from .models import Gallery

class GalleryForm(ModelForm):

    class Meta:
        model = Gallery
        fields = [
            'idImage',
            'image_galery'
        ]
        labels = {
            'idImage': 'ID Imagen',
            'image_galery': 'Imagen Galeria'
        }
        widgets = {
            'idImage': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Codigo Imagen'}),
            'image_galery': forms.FileInput(attrs={'class':'form-control'})
        }
        