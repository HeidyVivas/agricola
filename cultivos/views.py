from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Cultivo, Variedad, Produccion
from .serializers import CultivoSerializer, VariedadSerializer, ProduccionSerializer
from .filters import CultivoFilter, VariedadFilter, ProduccionFilter
from rest_framework import filters as drf_filters
from django.db.models import Sum

class CultivoViewSet(viewsets.ModelViewSet):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer
    filterset_class = CultivoFilter
    filter_backends = (drf_filters.SearchFilter, drf_filters.OrderingFilter, )
    search_fields = ('nombre',)
    ordering_fields = ('nombre', 'id')

class VariedadViewSet(viewsets.ModelViewSet):
    queryset = Variedad.objects.select_related('cultivo').all()
    serializer_class = VariedadSerializer
    filterset_class = VariedadFilter
    filter_backends = (drf_filters.SearchFilter, drf_filters.OrderingFilter, )
    search_fields = ('nombre',)
    ordering_fields = ('nombre', 'id')

class ProduccionViewSet(viewsets.ModelViewSet):
    queryset = Produccion.objects.select_related('variedad__cultivo').all()
    serializer_class = ProduccionSerializer
    filterset_class = ProduccionFilter
    filter_backends = (drf_filters.SearchFilter, drf_filters.OrderingFilter, )
    search_fields = ('ciclo',)
    ordering_fields = ('fecha_inicio', 'cantidad_planeada')

    @action(detail=False, methods=['get'])
    def resumen_por_cultivo(self, request):
        """
        Endpoint adicional: retorna para cada cultivo:
         - total cantidad_planeada (sum)
         - número de producciones
        Permite filtrar por cultivo id (?cultivo=1) o por rango de fecha_inicio.
        """
        qs = self.filter_queryset(self.get_queryset())

        cultivo_id = request.query_params.get('cultivo')
        if cultivo_id:
            qs = qs.filter(variedad__cultivo__id=cultivo_id)

        data = qs.values('variedad__cultivo__id', 'variedad__cultivo__nombre').annotate(
            total_planeado=Sum('cantidad_planeada'),
            producciones_count=Sum(1)
        )

        # normalizar respuesta
        result = []
        for item in data:
            result.append({
                'cultivo_id': item['variedad__cultivo__id'],
                'cultivo': item['variedad__cultivo__nombre'],
                'total_planeado': float(item['total_planeado'] or 0),
                'producciones_count': int(item['producciones_count'] or 0)
            })
        return Response(result, status=status.HTTP_200_OK)
