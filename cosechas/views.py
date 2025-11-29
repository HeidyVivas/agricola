
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from django.db.models import Avg

from .models import Cultivo, Cosecha
from .serializers import CultivoSerializer, CosechaSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class MiVista(APIView):
    permission_classes = [IsAuthenticated]

class CultivoViewSet(ModelViewSet):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer


class CosechaViewSet(ModelViewSet):
    queryset = Cosecha.objects.all()
    serializer_class = CosechaSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["cultivo", "fecha_cosecha"]

    @action(detail=False, methods=["get"])
    def promedio(self, request):
        promedio = Cosecha.objects.all().aggregate(Avg("cantidad"))["cantidad__avg"]
        return Response({"promedio_cosecha_kg": promedio})

