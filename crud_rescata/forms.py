from django import forms
from django.forms import ModelForm
from .models import Mascota

class Mascotaform(ModelForm):

    class Meta:
        model = Mascota
        fields = [
            'idMascota',
            'nombre',
            'image_mascota',
            'edad',
            'tipo',

        ]
        labels = {
            'idMascota': 'Codigo Mascota',
            'nombre': 'Nombre',
            'image_mascota': 'Imagen',
            'edad': 'edad',
            'tipo': 'tipo',
        }
        widgets = {
            'idMascota' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Codigo Mascota'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}),
            'image_mascota' : forms.FileInput(attrs={'class':'form-control'}),
            'edad' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Edad'}),
            'tipo' : forms.Select(attrs={'class':'form-control', 'placeholder': 'Tipo Mascota'}),
        }