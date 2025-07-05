from django.db import models

# Create your models here.
class Billet(models.Model):
    user = models.CharField()
    from_reserve = models.CharField(null=True)
    to_reserve = models.CharField(null=True)
    duree = models.CharField(null=True)
    num_salle = models.CharField()
    equipements = models.JSONField()
    servises = models.JSONField()
    type = models.CharField()
    qr_code = models.CharField()
    prix = models.CharField()
    status = models.CharField()

