from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer
from .mixins import BasculaGroupMemberMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



# Create your views here.
class ClienteViewSet(BasculaGroupMemberMixin,viewsets.ModelViewSet): #Esto es una vista basada en clases que hereda de viewsets.ModelViewSet y de BasculaGroupMemberMixin: este mixin es una clase que se encarga de validar que el usuario pertenezca al grupo Bascula
    queryset = Client.objects.all()
    serializer_class = ClientSerializer