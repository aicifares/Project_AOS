from django.db import models

# Create your models here.


class Reservation(models.Model):
    STATUT_CHOICES = [
        ('EN_ATTENTE', 'En attente'),
        ('CONFIRMEE', 'Confirmée'),
        ('ANNULEE', 'Annulée'),
    ]

    client_id    = models.IntegerField()
    table_id     = models.IntegerField()
    date         = models.DateField()
    heure        = models.TimeField()
    nb_personnes = models.IntegerField()
    statut       = models.CharField(max_length=20, choices=STATUT_CHOICES, default='EN_ATTENTE')
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Réservation #{self.id} - Table {self.table_id} - {self.date} {self.heure}"

    class Meta:
        ordering = ['-created_at']