from django.db import models
from unittest.util import _MAX_LENGTH
from django.utils.translation import gettext_lazy as _

# Create your models here.
class ListaPrecio (models.Model):
    codListaPrecio=models.CharField(max_length=50, verbose_name="Cod Lista Precio")
    nomListaPrecio=models.CharField(max_length=50, verbose_name="Nom Lista Precio")
    tipoLista=models.CharField(max_length=50, verbose_name="Tipo Lista")
    class Estado(models.TextChoices):
      ACTIVO='1', _('Activo')
      INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1,choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")


    def __str__(self):
        fila = "Nombre: "+ self.nomListaPrecio + " - Tipo: " + self.tipoLista 
        return fila