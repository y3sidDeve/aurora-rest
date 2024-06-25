from django.db import models

# importamos el usuario de django
from django.contrib.auth.models import User
from entrances.models import DetalleEntrada


# Create your models here.

class Asignacion(models.Model):
    id_detalle_entrada = models.ForeignKey(
        DetalleEntrada, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
