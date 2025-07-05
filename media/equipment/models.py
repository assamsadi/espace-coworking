from django.db import models

# Create your models here.
class Equipement(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    categorie = models.CharField(max_length=255)
    prix = models.IntegerField()
    photo = models.CharField()
    def __str__(self):
        return self.nom
