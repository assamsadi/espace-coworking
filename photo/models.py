# models.py
from django.db import models

class Photo(models.Model):
    file = models.ImageField(upload_to='photos/')
    def __str__(self):
        return self.file.url
    
