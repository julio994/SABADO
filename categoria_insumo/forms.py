from django import forms
from .models import Categoria_insumo

class CategoriaInsumoForm(forms.ModelForm):
    class Meta:
        model = Categoria_insumo
        fields = ['name', 'description']
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }