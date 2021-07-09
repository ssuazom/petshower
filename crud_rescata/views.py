from django.shortcuts import render

# Create your views here.

def rescata(request):
    return render(request, "crud_rescata/rescata_amigo.html")

def rescata_user(request):
    return render(request, "crud_rescata/rescata_amigo_user.html")

