from django.db import models
from django.utils import timezone

# Create your models here.
class Abonne (models.Model):
    user =  models.CharField()
    type =  models.CharField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField()

