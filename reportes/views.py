# reportes/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from cultivos.models import Cultivo
from cosechas.models import Cosecha
from perdidas.models import Perdida
from django.db.models import Avg, Sum

@api_view(['GET'])
def indicadores(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    
    # Filtrar por rango de fechas
    cosechas = Cosecha.objects.all()
    perdidas = Perdida.objects.all()
    
    if fecha_inicio:
        cosechas = cosechas.filter(fecha__gte=fecha_inicio)
        perdidas = perdidas.filter(fecha__gte=fecha_inicio)
    if fecha_fin:
        cosechas = cosechas.filter(fecha__lte=fecha_fin)
        perdidas = perdidas.filter(fecha__lte=fecha_fin)

    total_cosechas = cosechas.aggregate(total=Sum('cantidad_kg'))['total'] or 0
    promedio_por_cultivo = cosechas.values('cultivo__nombre').annotate(promedio=Avg('cantidad_kg'))
    porcentaje_perdidas = perdidas.aggregate(total_perdida=Sum('porcentaje'))['total_perdida'] or 0

    return Response({
        "total_cosechas_kg": total_cosechas,
        "promedio_por_cultivo": list(promedio_por_cultivo),
        "porcentaje_total_perdidas": porcentaje_perdidas,
    })

@api_view(['GET'])
def proyeccion_rendimiento(request, cultivo_id):
    cultivo = Cultivo.objects.get(id=cultivo_id)
    cosechas = Cosecha.objects.filter(cultivo=cultivo)
    perdidas = Perdida.objects.filter(cultivo=cultivo)

    promedio_cosechas = cosechas.aggregate(promedio=Avg('cantidad_kg'))['promedio'] or 0
    total_perdidas = perdidas.aggregate(total=Sum('porcentaje'))['total'] or 0

    rendimiento_proyectado = promedio_cosechas * (1 - total_perdidas/100)

    return Response({
        "cultivo": cultivo.nombre,
        "promedio_historico": promedio_cosechas,
        "perdidas_acumuladas": total_perdidas,
        "rendimiento_proyectado": rendimiento_proyectado
    })