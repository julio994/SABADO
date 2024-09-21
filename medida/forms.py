from django import forms
from .models import Medida

class MedidaForm(forms.ModelForm):
    class Meta:
        model = Medida
        fields = ['tipo_medida', 'description']  # Los campos que quieres incluir en el formulario
        labels = {
            'tipo_medida': 'Tipo de Medida',
            'description': 'Descripción',
        }
        widgets = {
            'tipo_medida': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }