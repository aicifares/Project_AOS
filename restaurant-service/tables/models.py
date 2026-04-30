from django.db import models

# Create your models here.
from django.db import models

class Table(models.Model):

    LOCALISATION_CHOICES = [
        ('interieur', 'Intérieur'),
        ('terrasse', 'Terrasse'),
        ('salon_prive', 'Salon Privé'),
    ]

    STATUT_CHOICES = [
        ('disponible', 'Disponible'),
        ('indisponible', 'Indisponible'),
    ]

    numero       = models.CharField(max_length=10)
    capacite     = models.IntegerField()
    localisation = models.CharField(
                        max_length=20,
                        choices=LOCALISATION_CHOICES,
                        default='interieur'
                    )
    statut       = models.CharField(
                        max_length=20,
                        choices=STATUT_CHOICES,
                        default='disponible'
                    )
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Table {self.numero} ({self.capacite} personnes)"