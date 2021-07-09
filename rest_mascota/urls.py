from django.urls import path
from rest_mascota.views import lista_mascotas, detalle_mascota

urlpatterns = [
    path('lista_mascotas', lista_mascotas, name="lista_mascotas"),
    path('detalle_mascota/<id>', detalle_mascota, name="detalle_mascota"),
]