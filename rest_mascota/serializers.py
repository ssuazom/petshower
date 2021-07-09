from rest_framework import serializers
from crud_rescata.models import Mascota

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ['idMascota', 'nombre', 'image_mascota', 'edad', 'tipo']