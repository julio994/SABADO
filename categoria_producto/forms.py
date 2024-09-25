from django import forms
from .models import Categoria_producto

class CategoriaProductoForm(forms.ModelForm):
    class Meta:
        model = Categoria_producto
        fields = ['nombre', 'descripcion']
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

