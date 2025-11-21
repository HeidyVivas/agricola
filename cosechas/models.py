from django.db import models
from cultivos.models import Cultivo

class Cosecha(models.Model):
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, related_name='cosechas')
    fecha_cosecha = models.DateField()
    cantidad_kg = models.DecimalField(max_digits=10, decimal_places=2)
    calidad = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Cosecha {self.cultivo.nombre} - {self.cantidad_kg} kg"
