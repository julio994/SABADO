from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def producto(request):
    product= Producto.objects.all()
    return render(request,"producto/producto.html",{"product":product})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo producto en la base de datos
            return redirect('producto_list')  # Redirige a la lista de productos o a otra página
    else:
        form = ProductoForm()

    return render(request, 'producto/crear_producto.html', {'form': form})