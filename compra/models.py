from django.db import models
from insumo.models import Insumo
from medida.models import Medida

class Compra(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'Compra {self.id} - {self.fecha}'
    
    # Método para actualizar el total sumando los valores de los detalles asociados
    def actualizar_total(self):
        total_detalles = sum(detalle.valor * detalle.cantidad for detalle in self.detalles.all())
        self.total = total_detalles
        self.save()

        def save(self, *args, **kwargs):
                self.actualizar_total()  # Llama a actualizar_total antes de guardar
                super().save(*args, **kwargs)  # Llama al método save de la clase padre

class CompraDetalle(models.Model):
    compra = models.ForeignKey(Compra, related_name='detalles', on_delete=models.CASCADE)  # Relación uno a muchos con Compra
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)  # Relación uno a muchos con Insumo
    medida = models.ForeignKey(Medida, on_delete=models.CASCADE)  # Relación uno a muchos con Medida
    cantidad = models.IntegerField(default=0)  # Cantidad de insumos
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Precio del insumo

    def __str__(self):
        return f'{self.insumo.nombre} - {self.cantidad} '

    # Sobrescribimos el método save para que, al guardar un detalle, actualice el total en la compra
    def save(self, *args, **kwargs):
        super(CompraDetalle, self).save(*args, **kwargs)
        self.compra.actualizar_total()  # Llamar a actualizar_total de Compra después de guardar un detalle
