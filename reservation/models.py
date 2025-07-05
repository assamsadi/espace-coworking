from django.db import models

# Create your models here.
class Reservation(models.Model):
    user = models.CharField()
    from_reserve = models.CharField(null=True)
    to_reserve = models.CharField(null=True)
    duree = models.CharField(null=True)
    num_salle = models.CharField()
    num_ticket = models.CharField()
    equipements = models.JSONField()
    servises = models.JSONField()
    status = models.CharField( default="pas encore")
    type = models.CharField()
    prix = models.CharField()
    date = models.CharField(null=True)
    piament = models.CharField(null=True , default="pas encore")

