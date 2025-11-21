from django.db import models

TIPO_CULTIVO_CHOICES = [
    ('maiz', 'Maíz'),
    ('trigo', 'Trigo'),
    ('arroz', 'Arroz'),
    ('frijol', 'Frijol'),
    ('otro', 'Otro'),
]

class Cultivo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPO_CULTIVO_CHOICES)
    area_hectareas = models.DecimalField(max_digits=7, decimal_places=2)
    fecha_siembra = models.DateField()
    productor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"
