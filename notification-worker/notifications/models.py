from django.db import models

class Notification(models.Model):
    
    TYPE_CHOICES = [
        ('CONFIRMATION', 'Confirmation'),
        ('ANNULATION', 'Annulation'),
    ]
    
    STATUT_CHOICES = [
        ('ENVOYEE', 'Envoyée'),
        ('ECHOUEE', 'Échouée'),
    ]
    # Ce que ce modèle représente :
    # Chaque fois qu'un email est envoyé, on enregistre une ligne dans la base de données avec :

    reservation_id = models.IntegerField()
    client_email   = models.EmailField()
    type           = models.CharField(max_length=20, choices=TYPE_CHOICES)
    statut         = models.CharField(max_length=10, choices=STATUT_CHOICES)
    sent_at        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} → {self.client_email} [{self.statut}]"