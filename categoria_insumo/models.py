from django.db import models

class Categoria_insumo(models.Model):
    name = models.CharField(max_length=100, verbose_name="nombre")
    description = models.TextField(max_length=200, verbose_name="descripcion")


    def __str__(self):
        return self.name
