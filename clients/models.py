from django.db import models

# Create your models here.
class Client(models.Model):
    id_cliente = models.CharField(max_length=50, primary_key=True, unique=True, blank=False)
    tipo_empresa = models.BooleanField(default=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    direccion = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    nombre_empresa = models.CharField(max_length=100, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True)
    apellido = models.CharField(max_length=100, blank=True)