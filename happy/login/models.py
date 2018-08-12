from django.db import models

class Information(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    birth_year = models.CharField(max_length=100)
    birth_month = models.CharField(max_length=100)
    birth_day = models.CharField(max_length=100)
    channel = models.CharField(max_length=100)
    referral_code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
