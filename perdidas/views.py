# perdidas/views.py
from rest_framework import viewsets, filters
from .models import Perdida
from .serializers import PerdidaSerializer
from django_filters.rest_framework import DjangoFilterBackend

class PerdidaViewSet(viewsets.ModelViewSet):
    queryset = Perdida.objects.all()
    serializer_class = PerdidaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['tipo', 'fecha']  # filtros obligatorios
    ordering_fields = ['fecha', 'porcentaje']