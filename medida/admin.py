from django.contrib import admin
from .models import Medida
# Register your models here.
class MedidaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Medida,MedidaAdmin)
