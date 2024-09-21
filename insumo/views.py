from django.shortcuts import render, redirect
from .models import Insumo
from .forms import InsumoForm

def insumo(request):
    insu= Insumo.objects.all()
    return render(request,"insumo/insumo.html",{"insu":insu})

def crear_insumo(request):
    if request.method == 'POST':
        form = InsumoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('insumo_page')  # Redirige a la lista de insumos después de guardar
    else:
        form = InsumoForm()
    
    return render(request, 'insumo/crear_insumo.html', {'form': form})