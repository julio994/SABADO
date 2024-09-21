from django.contrib import admin
from .models import Insumo
# Register your models here.
class InsumoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Insumo,InsumoAdmin)
