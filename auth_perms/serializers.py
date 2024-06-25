from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class AsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Asignacion
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


        


        
