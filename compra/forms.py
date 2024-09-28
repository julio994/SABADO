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

# Formset para manejar múltiples CompraDetalle
CompraDetalleFormSet = inlineformset_factory(
    Compra, CompraDetalle, 
    form=CompraDetalleForm, 
    extra=10,  # Puedes ajustar el número de formularios extra a mostrar
    can_delete=True  # Permite eliminar detalles si es necesario
)