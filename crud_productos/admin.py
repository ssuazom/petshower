from django.contrib import admin
from .models import Marca
from .models import Producto

# Register your models here.
admin.site.register(Marca)
admin.site.register(Producto)
