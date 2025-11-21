from rest_framework import serializers
from .models import Cultivo, Variedad, Produccion
from django.db.models import Sum
from .models import Produccion

class CultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultivo
        fields = ['id', 'nombre', 'descripcion']

class VariedadSerializer(serializers.ModelSerializer):
    cultivo = serializers.PrimaryKeyRelatedField(queryset=Cultivo.objects.all())

    class Meta:
        model = Variedad
        fields = ['id', 'cultivo', 'nombre', 'descripcion']

    def validate_nombre(self, value):
        if not value.strip():
            raise serializers.ValidationError("El nombre de la variedad no puede estar vacío.")
        return value

    def validate(self, data):
        cultivo = data.get('cultivo') or getattr(self.instance, 'cultivo', None)
        nombre = data.get('nombre') or getattr(self.instance, 'nombre', None)
        if cultivo and nombre:
            qs = Variedad.objects.filter(cultivo=cultivo, nombre__iexact=nombre)
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise serializers.ValidationError("Ya existe una variedad con ese nombre para este cultivo.")
        return data

class ProduccionSerializer(serializers.ModelSerializer):
    variedad = serializers.PrimaryKeyRelatedField(queryset=Variedad.objects.all())

    class Meta:
        model = Produccion
        fields = [
            'id', 'variedad', 'ciclo', 'fecha_inicio', 'fecha_fin',
            'cantidad_planeada', 'unidad', 'estado', 'created_at', 'updated_at',
        ]
        read_only_fields = ('created_at', 'updated_at')

    def validate(self, data):
        # fecha_inicio and fecha_fin logic
        fecha_inicio = data.get('fecha_inicio') or getattr(self.instance, 'fecha_inicio', None)
        fecha_fin = data.get('fecha_fin') or getattr(self.instance, 'fecha_fin', None)
        cantidad = data.get('cantidad_planeada') or getattr(self.instance, 'cantidad_planeada', None)

        if fecha_inicio and fecha_fin and fecha_fin < fecha_inicio:
            raise serializers.ValidationError("fecha_fin debe ser posterior o igual a fecha_inicio.")

        if cantidad is not None and cantidad < 0:
            raise serializers.ValidationError("cantidad_planeada no puede ser negativa.")

        # Ensure unique (variedad, ciclo)
        variedad = data.get('variedad') or getattr(self.instance, 'variedad', None)
        ciclo = data.get('ciclo') or getattr(self.instance, 'ciclo', None)
        if variedad and ciclo:
            qs = Produccion.objects.filter(variedad=variedad, ciclo__iexact=ciclo)
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise serializers.ValidationError("Ya existe una producción para esa variedad y ciclo.")

        return data
