from django.db import models
from insumo.models import Insumo
from medida.models import Medida

class Compra(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'Compra {self.id} - {self.fecha}'
    

class CompraDetalle(models.Model):
        compra = models.ForeignKey(Compra, on_delete=models.CASCADE)  # Relación uno a muchos con Compra
        insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)  # Relación uno a muchos con Producto
        medida = models.ForeignKey(Medida, on_delete=models.CASCADE)  # Relación uno a muchos con Producto
        cantidad = models.IntegerField(default=0)  # Para productos como cervezas
        valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)

        def __str__(self):
                return f'{self.insumo.name} - {self.cantidad} '
    