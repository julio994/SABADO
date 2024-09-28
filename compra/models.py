from django.db import models
from insumo.models import Insumo
from medida.models import Medida

class Compra(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'Compra {self.id} - {self.fecha}'
    
    def calcular_total(self):
        # Sumar los valores de todos los detalles de esta compra
        total = sum(detalle.valor for detalle in self.detalles.all())
        return total

    def save(self, *args, **kwargs):
        # Si es una instancia nueva (sin PK), guardar primero para asignar un ID
        if self.pk is None:
            super().save(*args, **kwargs)  # Guardar por primera vez
        
        # Calcular el total después de que se haya guardado la compra
        self.total = self.calcular_total()
        # Guardar nuevamente para actualizar el total
        super().save(*args, **kwargs)
class CompraDetalle(models.Model):
    compra = models.ForeignKey(Compra, related_name='detalles', on_delete=models.CASCADE)  # Relación uno a muchos con Compra
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)  # Relación uno a muchos con Insumo
    medida = models.ForeignKey(Medida, on_delete=models.CASCADE)  # Relación uno a muchos con Medida
    cantidad = models.IntegerField(default=0)  # Cantidad de insumos
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Precio del insumo

    def __str__(self):
        return f'{self.insumo.nombre} - {self.cantidad} '

    def save(self, *args, **kwargs):
        # Guardar el detalle de la compra normalmente
        super().save(*args, **kwargs)
        # Actualizar el total de la compra después de guardar un detalle
        self.compra.save()