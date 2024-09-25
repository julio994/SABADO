from django.shortcuts import render, redirect
from .models import Categoria_producto
from .forms import CategoriaProductoForm


def categoria_producto(request):
    categop= Categoria_producto.objects.all()
    return render(request,"categoria_producto/categoria_producto.html",{"categop":categop})

def crear_categoria_producto(request):
    if request.method == 'POST':
        form = CategoriaProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoriap_list')
    else:
        form = CategoriaProductoForm()
    
    return render(request, 'categoria_producto/crear_categoria_producto.html', {'form': form})