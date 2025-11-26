# perdidas/serializers.py
from rest_framework import serializers
from .models import Perdida

class PerdidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perdida
        fields = '__all__'

    def validate_porcentaje(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("El porcentaje debe estar entre 0 y 100")
        return value