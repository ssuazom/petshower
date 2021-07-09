from django.shortcuts import render, redirect, reverse
from .models import Veterinarios
from .forms import Veterinarioform

# Create your views here.

def socios(request):
    veterinario = Veterinarios.objects.all() 
    return render(request, "crud_veterinarios/veterinarios_socios.html",{'veterinario':veterinario})


def socios_user(request):
    veterinario = Veterinarios.objects.all() 
    return render(request, "crud_veterinarios/veterinarios_socios_user.html",{'veterinario':veterinario})


def add_vet(request):
    if request.method == 'POST':
        form_veterinario = Veterinarioform(request.POST or None, request.FILES or None)
        if form_veterinario.is_valid():
            idVeterinario = form_veterinario.cleaned_data.get("idVeterinario")
            nombre = form_veterinario.cleaned_data.get("nombre")
            descripcion = form_veterinario.cleaned_data.get("descripcion")
            image_veterinario = form_veterinario.cleaned_data.get("image_veterinario")
            link_facebook = form_veterinario.cleaned_data.get("link_facebook")
            link_instagram = form_veterinario.cleaned_data.get("link_instagram")
            link_whatsapp = form_veterinario.cleaned_data.get("link_whatsapp")
            link_twitter = form_veterinario.cleaned_data.get("link_twitter")
            obj = Veterinarios.objects.create(
                idVeterinario = idVeterinario,
                nombre = nombre,
                descripcion = descripcion,
                image_veterinario = image_veterinario,
                link_facebook = link_facebook,
                link_instagram = link_instagram,
                link_whatsapp = link_whatsapp,
                link_twitter = link_twitter
            )
            obj.save()
            return redirect(reverse('add_veterinario') + "?OK")
        else:
            return redirect(reverse('add_veterinario') + "?FAIL")
    else:
        form_veterinario = Veterinarioform
    return render(request,"crud_veterinarios/add_veterinario.html",{'form':form_veterinario})



# Vista modificar Veterinario
def update_veterinario(request, idVeterinario):
    upd_veterinario = Veterinarios.objects.get(idVeterinario=idVeterinario)
    form_veterinario = Veterinarioform(instance = upd_veterinario)

    if request.method == 'POST':
        form_veterinario = Veterinarioform(request.POST or None, request.FILES or None, instance=upd_veterinario)
        if form_veterinario.is_valid():
            form_veterinario.save()
            return redirect(reverse('socios') + "?OK")
        else:
            return redirect(reverse('update_veterinario') + idVeterinario)

    return render(request, "crud_veterinarios/update_veterinario.html", {'form':form_veterinario})



# Vista Eliminar Veterinario
def delete_veterinario(request,idVeterinario):
    dlt_veterinario = Veterinarios.objects.get(idVeterinario=idVeterinario)
    dlt_veterinario.delete()
    return redirect(to='socios')
