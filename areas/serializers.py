from rest_framework import serializers
from . import models

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Area
        fields = '__all__'
        



