from django.db import models

# Create your models here.

class Cultivo(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Variedad(models.Model):
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, related_name='variedades')
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)

    class Meta:
        unique_together = ('cultivo', 'nombre')
        ordering = ['cultivo__nombre', 'nombre']

    def __str__(self):
        return f"{self.cultivo.nombre} - {self.nombre}"

class Produccion(models.Model):
    """
    Representa un ciclo de producción para una variedad (ciclo, fechas, cantidad planeada).
    """
    variedad = models.ForeignKey(Variedad, on_delete=models.PROTECT, related_name='producciones')
    ciclo = models.CharField(max_length=80)  # e.g. "2025-01", "Ciclo A"
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    cantidad_planeada = models.DecimalField(max_digits=12, decimal_places=3)  # e.g. kg
    unidad = models.CharField(max_length=20, default='kg')
    estado = models.CharField(max_length=30, default='activo')  # activo, finalizado, cancelado

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_inicio']
        unique_together = ('variedad', 'ciclo')

    def __str__(self):
        return f"{self.variedad} | {self.ciclo}"
