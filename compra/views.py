from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import Compra, CompraDetalle
from .forms import CompraForm, CompraDetalleForm
# Vista para listar las compras
def listar_compras(request):
    compras = Compra.objects.all()
    return render(request, 'compra/compra_list.html', {'compras': compras})

def listar_detallecompras(request):
    detallecompras = CompraDetalle.objects.all()
    return render(request, 'compra/compra_list.html', {'detallecompras': detallecompras})
""""
def crear_compra_y_detalles(request):
    if request.method == 'POST':
        compra_form = CompraForm(request.POST)  # Formulario de compra
        formset = CompraDetalleFormSet(request.POST)  # Formset para detalles de compra

        if compra_form.is_valid() and formset.is_valid():
            compra = compra_form.save(commit=False)  # Guardamos la compra sin hacer commit
            compra.save()  # Guardamos la compra para obtener su ID

            detalles = formset.save(commit=False)  # Guardamos los detalles sin hacer commit
            for detalle in detalles:
                detalle.compra = compra  # Asociamos el detalle a la compra
                detalle.save()  # Guardamos cada detalle

            # Redirigir a una vista, como la lista de compras
            return redirect('compra-list')
    else:
        compra_form = CompraForm()
        formset = CompraDetalleFormSet()

    return render(request, 'compra/compra_y_detalle_form.html', {
        'compra_form': compra_form,
        'formset': formset,
    })

"""
def crear_compra_y_detalles(request):
    if request.method == 'POST':
        compra_form = CompraForm(request.POST)
        detalle_forms = [CompraDetalleForm(request.POST, prefix=str(i)) for i in range(len(request.POST.getlist('insumo')))]
        
        if compra_form.is_valid() and all(df.is_valid() for df in detalle_forms):
            compra = compra_form.save()
            for detalle_form in detalle_forms:
                detalle = detalle_form.save(commit=False)
                detalle.compra = compra  # Asocia el detalle con la compra
                detalle.save()
            return redirect('success_url')  # Redirige a una página de éxito

    else:
        compra_form = CompraForm()
        detalle_forms = [CompraDetalleForm(prefix=str(i)) for i in range(1)]  # Inicializa al menos uno

    return render(request, 'compra/compra_y_detalle_form.html', {
        'compra_form': compra_form,
        'detalle_forms': detalle_forms,
    })
