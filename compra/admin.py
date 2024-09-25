from django.contrib import admin
from .models import Compra, CompraDetalle
# Register your models here.


class CompraDetalleAdmin(admin.TabularInline):
    model= CompraDetalle
    extra=0


class CompraAdmin(admin.ModelAdmin):
    model= Compra
    inlines=[
        CompraDetalleAdmin
    ]
admin.site.register(Compra,CompraAdmin)


