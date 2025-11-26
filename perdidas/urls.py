# perdidas/urls.py
from rest_framework.routers import DefaultRouter
from .views import PerdidaViewSet

router = DefaultRouter()
router.register(r'perdidas', PerdidaViewSet, basename='perdidas')

urlpatterns = router.urls