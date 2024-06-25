from django.db import models
from clients.models import Client
from materials.models import Material
from areas.models import Area
from django.contrib.auth.models import User

# Create your models here.
class Entrances(models.Model):
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    fecha_hora_llegada = models.DateTimeField()
    estado = models.BooleanField(default=False)
    user_created = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    
class DetalleEntrada(models.Model):
    entrada = models.ForeignKey(Entrances, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Ruta de imagen de la entrada
    fotografia = models.CharField(max_length=255, blank=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, default=1) #este campo guarda el id del area en la base de datos