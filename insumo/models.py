from django.db import models
from django.utils import timezone
from categoria_insumo.models import Categoria_insumo
from medida.models import Medida
# Create your models here.

class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    categoria_insumo = models.ForeignKey(Categoria_insumo,verbose_name="Categoria", on_delete=models.CASCADE)
    medida= models.ForeignKey(Medida,verbose_name="Medida", on_delete=models.CASCADE)
    stock= models.IntegerField(default=0)

    def __str__(self):
        return self.nombre