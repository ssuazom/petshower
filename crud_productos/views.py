from django.shortcuts import render, redirect, reverse
from .models import Producto
from .forms import Productoform

# Create your views here.

def productos(request):
    Productos = Producto.objects.all()
    return render(request, "crud_productos/productos.html",{'Productos':Productos})


def productos_user(request):
    Productos = Producto.objects.all()
    return render(request, "crud_productos/productos_user.html",{'Productos':Productos})

def add_producto(request):
    if request.method == 'POST':
        form_producto = Productoform(request.POST or None, request.FILES or None)
        if form_producto.is_valid():
            idProducto = form_producto.cleaned_data.get("idProducto")
            nombre = form_producto.cleaned_data.get("nombre")
            descripcion = form_producto.cleaned_data.get("descripcion")
            image_producto = form_producto.cleaned_data.get("image_producto")
            precio = form_producto.cleaned_data.get("precio")
            stock = form_producto.cleaned_data.get("stock")
            marca = form_producto.cleaned_data.get("marca")
            obj = Producto.objects.create(
                idProducto = idProducto,
                nombre = nombre,
                descripcion = descripcion,
                image_producto = image_producto,
                precio = precio,
                stock = stock,
                marca = marca,
            )
            obj.save()
            return redirect(reverse('add_producto') + "?OK")
        else:
            return redirect(reverse('add_producto') + "?FAIL")
    else:
        form_producto = Productoform
    return render(request,"crud_productos/add_productos.html",{'form':form_producto})


# Vista modificar Producto
def update_producto(request, idProducto):
    udt_producto = Producto.objects.get(idProducto=idProducto)
    form_producto = Productoform(instance = udt_producto)

    if request.method == 'POST':
        form_producto = Productoform(request.POST or None, request.FILES or None, instance=udt_producto)
        if form_producto.is_valid():
            form_producto.save()
            return redirect(reverse('productos') + "?OK")
        else:
            return redirect(reverse('update_producto') + idProducto)

    return render(request, "crud_productos/update_productos.html", {'form':form_producto})


# Vista Eliminar Producto
def delete_producto(request,idProducto):
    dlt_producto = Producto.objects.get(idProducto=idProducto)
    dlt_producto.delete()
    return redirect(to='productos')