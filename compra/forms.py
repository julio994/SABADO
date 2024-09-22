from django import forms
from .models import Compra, CompraDetalle

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['total']

class CompraDetalleForm(forms.ModelForm):
    class Meta:
        model = CompraDetalle
        fields = ['insumo', 'medida', 'cantidad', 'valor']
