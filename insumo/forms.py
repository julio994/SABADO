from django import forms
from .models import Insumo


class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['nombre', 'categoria_insumo', 'medida', 'stock']
        labels = {
            'nombre': 'Nombre del Insumo',
            'categoria_insumo': 'Categoría del Insumo',
            'medida': 'Medida',
            'stock': 'Cantidad en Stock',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria_insumo': forms.Select(attrs={'class': 'form-control'}),
            'medida': forms.Select(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }