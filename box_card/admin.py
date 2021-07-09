from django.contrib import admin
from .models import Project
from .models import Gallery

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('create','updated')

admin.site.register(Project, ProjectAdmin)


class GalleryAdmin(admin.ModelAdmin):
    readonly_fields = ('create','updated')

admin.site.register(Gallery, GalleryAdmin)
