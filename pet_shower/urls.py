"""pet_shower URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from core import views as core_views
from box_card import views as box_card_views
from crud_conocenos import views as crud_conocenos_views
from crud_productos import views as crud_productos_views
from crud_veterinarios import views as crud_veterinarios_views
from crud_rescata import views as crud_rescata_views

from django.conf import settings

urlpatterns = [
    path('', box_card_views.home, name='home'),
    path('home_admin/', box_card_views.home_admin, name='home_admin'),
    path('home_user/', box_card_views.home_user, name='home_user'),
    path('conocenos/', crud_conocenos_views.conocenos, name='conocenos'),
    path('conocenos_user/', crud_conocenos_views.conocenos_user, name='conocenos_user'),
    path('productos/', crud_productos_views.productos, name='productos'),
    path('productos_user/', crud_productos_views.productos_user, name='productos_user'),
    path('contacto/', core_views.contacto, name='contacto'),
    path('socios/', crud_veterinarios_views.socios, name='socios'),
    path('socio_user/', crud_veterinarios_views.socios_user, name='socio_user'),
    path('add/', crud_conocenos_views.add_equipo, name='add_equipo'),
    path('update_equipo/<idIntegrante>',crud_conocenos_views.update_equipo, name='update_equipo'),
    path('delete_equipo/<idIntegrante>',crud_conocenos_views.delete_equipo, name='delete_equipo'),
    path('add_producto/',crud_productos_views.add_producto, name='add_producto'),
    path('update_producto/<idProducto>',crud_productos_views.update_producto, name='update_producto'),
    path('delete_producto/<idProducto>',crud_productos_views.delete_producto, name='delete_producto'),
    path('add_veterinario/',crud_veterinarios_views.add_vet, name='add_veterinario'),
    path('update_veterinario/<idVeterinario>',crud_veterinarios_views.update_veterinario, name="update_veterinario"),
    path('delete_veterinario/<idVeterinario>',crud_veterinarios_views.delete_veterinario, name="delete_veterinario"),
    path('rescata/',crud_rescata_views.rescata, name="rescata"),
    path('rescata_user/',crud_rescata_views.rescata_user, name="rescata_user"),
    path('api/', include('rest_mascota.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
