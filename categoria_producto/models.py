from django.db import models

class Categoria_producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="nombre")
    descripcion = models.TextField(max_length=200, verbose_name="descripcion")


    def __str__(self):
        return self.nombre

