from django.contrib import admin
from .models import Categoria_producto
# Register your models here.
class CategoriaProductoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Categoria_producto,CategoriaProductoAdmin)
