from django.contrib import admin
from .models import Producto, Receta, Insumo

class RecetaInline(admin.TabularInline):
    model = Receta
    extra = 1

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'insumo', 'cantidad')
