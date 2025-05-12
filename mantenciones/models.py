from django.db import models

class Mantencion(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('proceso', 'En proceso'),
        ('finalizada', 'Finalizada'),
    ]

    dueño = models.CharField(max_length=100)
    patente = models.CharField(max_length=10)
    kilometraje = models.PositiveIntegerField()
    tipo = models.CharField(max_length=100)
    fecha = models.DateField()
    observaciones = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return f"{self.patente} - {self.tipo} ({self.fecha})"
