# perdidas/models.py
from django.db import models
from cultivos.models import Cultivo  # FK a la app Cultivos

TIPO_PERDIDA_CHOICES = [
    ('plaga', 'Plaga'),
    ('clima', 'Clima'),
    ('manejo', 'Manejo'),
    ('otro', 'Otro'),
]

class Perdida(models.Model):
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, related_name='perdidas')
    tipo = models.CharField(max_length=50, choices=TIPO_PERDIDA_CHOICES)
    causa = models.TextField()
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.tipo} - {self.porcentaje}%"