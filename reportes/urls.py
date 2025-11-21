# reportes/urls.py
from django.urls import path
from .views import indicadores, proyeccion_rendimiento

urlpatterns = [
    path('indicadores/', indicadores, name='indicadores'),
    path('proyeccion/<int:cultivo_id>/', proyeccion_rendimiento, name='proyeccion_rendimiento'),
]