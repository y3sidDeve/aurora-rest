from rest_framework import serializers

from . import models

class EntranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Entrances
        fields = '__all__'
        

class DetalleEntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DetalleEntrada
        fields = '__all__'
        

