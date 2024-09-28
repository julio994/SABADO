from django.db import models
from insumo.models import Insumo
from producto.models import Producto

class Receta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='recetas')
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.FloatField()  # Cantidad de insumo que se usa en la receta

    def __str__(self):
        return f'{self.producto.nombre} - {self.insumo.nombre} ({self.cantidad} {self.insumo.unidad_medida})'

