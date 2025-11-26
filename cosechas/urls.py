from rest_framework.routers import DefaultRouter
from .views import CosechaViewSet, LoteViewSet

router = DefaultRouter()
router.register(r'cosechas', CosechaViewSet, basename='cosechas')
router.register(r'lotes', LoteViewSet, basename='lotes')

urlpatterns = router.urls



