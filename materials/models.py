from django.db import models
from areas.models import Area

# Create your models here.
class Material(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
