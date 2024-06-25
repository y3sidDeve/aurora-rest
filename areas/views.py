from rest_framework import viewsets
from .models import Area
from .serializers import AreaSerializer

# Create your views here.
class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


