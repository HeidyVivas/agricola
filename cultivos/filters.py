import django_filters
from .models import Cultivo, Variedad, Produccion

class CultivoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(field_name='nombre', lookup_expr='icontains')
    # más filtros si se desea

    class Meta:
        model = Cultivo
        fields = ['nombre']

class VariedadFilter(django_filters.FilterSet):
    cultivo = django_filters.NumberFilter(field_name='cultivo__id')
    nombre = django_filters.CharFilter(field_name='nombre', lookup_expr='icontains')

    class Meta:
        model = Variedad
        fields = ['cultivo', 'nombre']

class ProduccionFilter(django_filters.FilterSet):
    ciclo = django_filters.CharFilter(field_name='ciclo', lookup_expr='icontains')
    variedad = django_filters.NumberFilter(field_name='variedad__id')
    cultivo = django_filters.NumberFilter(field_name='variedad__cultivo__id')
    fecha_inicio_min = django_filters.DateFilter(field_name='fecha_inicio', lookup_expr='gte')
    fecha_inicio_max = django_filters.DateFilter(field_name='fecha_inicio', lookup_expr='lte')
    fecha_fin_min = django_filters.DateFilter(field_name='fecha_fin', lookup_expr='gte')
    fecha_fin_max = django_filters.DateFilter(field_name='fecha_fin', lookup_expr='lte')
    cantidad_min = django_filters.NumberFilter(field_name='cantidad_planeada', lookup_expr='gte')
    cantidad_max = django_filters.NumberFilter(field_name='cantidad_planeada', lookup_expr='lte')

    class Meta:
        model = Produccion
        fields = [
            'ciclo', 'variedad', 'cultivo',
            'fecha_inicio_min', 'fecha_inicio_max',
            'fecha_fin_min', 'fecha_fin_max',
            'cantidad_min', 'cantidad_max'
        ]
