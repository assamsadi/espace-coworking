# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE = (
        ('admin', 'admin'),
        ('staff', 'ataff'),
        ('client', 'client'),
    )
    role = models.CharField(max_length=10, choices=ROLE, default='client')
    phone = models.CharField(max_length=15, blank=True, null=True)
    photo = models.CharField( blank=True, null=True)

    def __str__(self):
        return self.username

