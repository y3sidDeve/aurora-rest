from rest_framework import viewsets
from .models import Entrances, DetalleEntrada
from .serializers import EntranceSerializer, DetalleEntradaSerializer

# Create your views here.

class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrances.objects.all()
    serializer_class = EntranceSerializer


class DetalleEntradaViewSet(viewsets.ModelViewSet):
    queryset = DetalleEntrada.objects.all()
    serializer_class = DetalleEntradaSerializer
