from django.db import models


class Medida(models.Model):
    tipo_medida = models.CharField(max_length=100, verbose_name="tipo_medida")
    description = models.TextField(max_length=200, verbose_name="descripcion")


    def __str__(self):
        return self.tipo_medida