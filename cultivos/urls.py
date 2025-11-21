from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CultivoViewSet, VariedadViewSet, ProduccionViewSet

router = DefaultRouter()
router.register(r'cultivos', CultivoViewSet, basename='cultivo')
router.register(r'variedades', VariedadViewSet, basename='variedad')
router.register(r'producciones', ProduccionViewSet, basename='produccion')

urlpatterns = [
    path('', include(router.urls)),
]
