from django.shortcuts import render, redirect, get_object_or_404
from .models import Receta
from .forms import RecetaForm

# Lista de recetas
def receta_list(request):
    recetas = Receta.objects.all()
    return render(request, 'receta/receta_list.html', {'recetas': recetas})

# Crear receta
def receta_create(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receta_list')
    else:
        form = RecetaForm()
    return render(request, 'receta/receta_form.html', {'form': form})

def receta_detail(request, id):
    receta = get_object_or_404(Receta, id=id)
    return render(request, 'receta/receta_detail.html', {'receta': receta})

# Editar receta
def receta_update(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    if request.method == 'POST':
        form = RecetaForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('receta_list')
    else:
        form = RecetaForm(instance=receta)
    return render(request, 'receta/receta_form.html', {'form': form})
