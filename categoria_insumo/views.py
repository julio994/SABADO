from django.shortcuts import render, redirect
from .models import Categoria_insumo
from .forms import CategoriaInsumoForm

def categoria_insumo(request):
    categoi= Categoria_insumo.objects.all()
    return render(request,"categoria_insumo/categoria_insumo.html",{"categoi":categoi})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaInsumoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoriai_page')
    else:
        form = CategoriaInsumoForm()
    
    return render(request, 'categoria_insumo/crear_categoria.html', {'form': form})