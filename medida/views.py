from django.shortcuts import render
from .models import Medida

def medida(request):
    medi= Medida.objects.all()
    return render(request,"medida/medida.html",{"medi":medi})


from django.shortcuts import render, redirect
from .forms import MedidaForm

def crear_medida(request):
    if request.method == 'POST':
        form = MedidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medida_page')  # Redirige a la página deseada
    else:
        form = MedidaForm()
    
    return render(request, 'medida/crear_medida.html', {'form': form})