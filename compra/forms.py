from django import forms
from django.forms import inlineformset_factory
from .models import Compra, CompraDetalle

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['total']

class CompraDetalleForm(forms.ModelForm):
    class Meta:
        model = CompraDetalle
        fields = ['insumo', 'medida', 'cantidad', 'valor']

# Definimos un formset para CompraDetalle
CompraDetalleFormSet = inlineformset_factory(
    Compra, CompraDetalle,  # Relación Compra -> CompraDetalle
    form=CompraDetalleForm,
    extra=1,  # Número de formularios adicionales por defecto
    can_delete=True  # Permitir eliminar detalles de la compra
)