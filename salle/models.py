from django.db import models

# Create your models here.
class Salle(models.Model):
    name = models.CharField()
    description = models.TextField()
    categorie = models.CharField(max_length=255)
    prix = models.IntegerField()
    photo = models.CharField()
    equipments = models.JSONField(null=True)
    reservation_date = models.JSONField(null=True, default="[]")
    status = models.CharField(null=True)
