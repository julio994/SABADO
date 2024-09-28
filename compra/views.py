from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from .models import Compra, CompraDetalle
from .forms import CompraForm, CompraDetalleFormSet
# Vista para listar las compras
def listar_compras(request):
    compras = Compra.objects.all()
    return render(request, 'compra/compra_list.html', {'compras': compras})

def listar_detallecompras(request):
    detallecompras = CompraDetalle.objects.all()
    return render(request, 'compra/compra_list.html', {'detallecompras': detallecompras})

def crear_compra(request):
    if request.method == 'POST':
        compra_form = CompraForm(request.POST)
        formset = CompraDetalleFormSet(request.POST)

        if compra_form.is_valid() and formset.is_valid():
            compra = compra_form.save()
            detalles = formset.save(commit=False)
            for detalle in detalles:
                detalle.compra = compra  # Asocia cada detalle a la compra
                detalle.save()
            return redirect('compra-list')  # Redirige después de guardar
    else:
        compra_form = CompraForm()
        formset = CompraDetalleFormSet()

    return render(request, 'compra/crear_compra.html', {
        'compra_form': compra_form,
        'formset': formset,
    })


def detalle_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    detallecompras = CompraDetalle.objects.filter(compra=compra)

    return render(request, 'compra/detalle_compra.html', {
        'compra': compra,
        'detallecompras': detallecompras
    })