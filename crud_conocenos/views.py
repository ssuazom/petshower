from django.shortcuts import render, redirect, reverse
from .models import Equipo
from .forms import Equipoform

# Create your views here.

# Vista tabla equipo de Trabajo
def conocenos(request):
    Equipos = Equipo.objects.all()
    return render(request, "crud_conocenos/quienes_somos.html",{'Equipos':Equipos})


def conocenos_user(request):
    Equipos = Equipo.objects.all()
    return render(request, "crud_conocenos/quienes_somos_user.html",{'Equipos':Equipos})


# Vista envio formulario
def add_equipo(request):
    if request.method == 'POST':
        form_equipo = Equipoform(request.POST or None, request.FILES or None)
        if form_equipo.is_valid():
            idIntegrante = form_equipo.cleaned_data.get("idIntegrante")
            nombre = form_equipo.cleaned_data.get("nombre")
            description = form_equipo.cleaned_data.get("description")
            image_conoce = form_equipo.cleaned_data.get("image_conoce")
            link_facebook = form_equipo.cleaned_data.get("link_facebook")
            link_instagram = form_equipo.cleaned_data.get("link_instagram")
            link_whatsapp = form_equipo.cleaned_data.get("link_whatsapp")
            link_twitter = form_equipo.cleaned_data.get("link_twitter")
            obj = Equipo.objects.create(
                idIntegrante = idIntegrante,
                nombre = nombre,
                description = description,
                image_conoce = image_conoce,
                link_facebook = link_facebook,
                link_instagram = link_instagram,
                link_whatsapp = link_whatsapp,
                link_twitter = link_twitter
            )
            obj.save()
            return redirect(reverse('add_equipo') + "?OK")
        else:
            return redirect(reverse('add_equipo') + "?FAIL")
    else:
        form_equipo = Equipoform
    return render(request, "crud_conocenos/add_equipo.html", {'form':form_equipo})


# Vista modificar integrante
def update_equipo(request, idIntegrante):
    integrante = Equipo.objects.get(idIntegrante=idIntegrante)
    form_equipo = Equipoform(instance = integrante)

    if request.method == 'POST':
        form_equipo = Equipoform(request.POST or None, request.FILES or None, instance=integrante)
        if form_equipo.is_valid():
            form_equipo.save()
            return redirect(reverse('conocenos') + "?OK")
        else:
            return redirect(reverse('update_equipo') + idIntegrante)

    return render(request, "crud_conocenos/update_equipo.html", {'form':form_equipo})

# Vista Eliminar Integrante
def delete_equipo(request,idIntegrante):
    dlt_integrante = Equipo.objects.get(idIntegrante=idIntegrante)
    dlt_integrante.delete()
    return redirect(to='conocenos')
