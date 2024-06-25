from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'entrances', views.EntradaViewSet)
router.register(r'details', views.DetalleEntradaViewSet)

urlpatterns = router.urls
