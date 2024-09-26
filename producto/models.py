from django.db import models
from categoria_producto.models import Categoria_producto

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria_producto= models.ForeignKey(Categoria_producto,verbose_name="Categoria", on_delete=models.CASCADE)
    descripcion= models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre