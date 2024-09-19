from django.contrib import admin
from .models import Categoria_insumo
# Register your models here.
class CategoriaInsumoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Categoria_insumo,CategoriaInsumoAdmin)
