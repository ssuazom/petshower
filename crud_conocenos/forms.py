from django import forms
from django.forms import ModelForm
from .models import Equipo

class Equipoform(ModelForm):

    class Meta:
        model = Equipo
        fields = [
            'idIntegrante',
            'nombre',
            'description',
            'image_conoce',
            'link_facebook',
            'link_instagram',
            'link_whatsapp',
            'link_twitter'
        ]
        labels = {
            'idIntegrante': 'Codigo Integrante',
            'nombre': 'Nombre Completo',
            'description': 'Descripcion',
            'image_conoce': 'Imagen',
            'link_facebook': 'URL facebook',
            'link_instagram': 'URL Instagram',
            'link_whatsapp': 'URL whatsapp',
            'link_twitter': 'URL twitter'
        }
        widgets = {
            'idIntegrante' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Codigo Integrante'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre Completo'}),
            'description' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Descripcion'}),
            'image_conoce' : forms.FileInput(attrs={'class':'form-control'}),
            'link_facebook' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'URL Facebook'}),
            'link_instagram' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'URL Instagram'}),
            'link_whatsapp' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'URL Whatsapp'}),
            'link_twitter' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'URL Twitter'})
        }