from rest_framework import viewsets
from .models import Material
from .serializers import MaterialSerializer

# Create your views here.
class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    
