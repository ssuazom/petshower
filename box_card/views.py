from django.shortcuts import render
from django.http import JsonResponse
from .models import Project
from .models import Gallery
from .forms import GalleryForm


# Create your views here.
def home_admin(request):
    projects = Project.objects.all()
    galleries = Gallery.objects.all()
    return render(request, "box_card/index_admin.html", {'projects':projects, 'galleries':galleries})

def home_user(request):
    projects = Project.objects.all()
    galleries = Gallery.objects.all()

    return render(request, "box_card/index_user.html",{'projects':projects, 'galleries':galleries})


def home(request):
    projects = Project.objects.all()
    galleries = Gallery.objects.all()

    return render(request, "box_card/index.html",{'projects':projects, 'galleries':galleries})

def add_image(request):
    if request.method == 'POST':
        add_image = GalleryForm(request.POST or None, request.FILES or None)
        if form.is_valid ():
            response = JsonResponse ({"message": 'success'})
            response.status_code = 201 
            return response
        else:
            response = JsonResponse ({"errors": form.errors.as_json ()})
            response.status_code = 403
            return response

    return render(request, "box_card/index.html", {'form':add_image})



