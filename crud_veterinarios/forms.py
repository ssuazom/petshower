from django import forms
from django.forms import ModelForm
from .models import Veterinarios

class Veterinarioform(ModelForm):

    class Meta:
        model = Veterinarios
        fields = [
            'idVeterinario',
            'nombre',
            'descripcion',
            'image_veterinario',
            'link_facebook',
            'link_instagram',
            'link_whatsapp',
            'link_twitter'
        ]
        labels = {
            'idVeterinario': 'Codigo Veterinario',
            'nombre': 'Nombre Completo',
            'descripcion': 'Descripcion',
            'image_veterinario': 'Imagen',
            'link_facebook': 'URL facebook',
            'link_instagram': 'URL Instagram',
            'link_whatsapp': 'URL whatsapp',
            'link_twitter': 'URL twitter'
        }
        widgets = {
            'idVeterinario' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Codigo Veterinario'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre Completo'}),
            'descripcion' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Descripcion'}),
            'image_veterinario' : forms.FileInput(attrs={'class':'form-control'}),
            'link_facebook' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'URL Facebook'}),
            'link_instagram' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'URL Instagram'}),
            'link_whatsapp' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'URL Whatsapp'}),
            'link_twitter' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'URL Twitter'})
        }