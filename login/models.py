from django.db import models
<<<<<<< HEAD
from django.conf import settings

class Information(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    birth_year = models.IntegerField(blank=True)
    birth_month = models.IntegerField(blank=True)
    birth_day = models.IntegerField(blank=True)
    channel = models.CharField(max_length=100)
    referral_code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

=======

# Create your models here.
>>>>>>> 7f5d1551887abe6fb3e1badd8233aae6a2a164d5
