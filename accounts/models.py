from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Information(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    birth_year = models.IntegerField(blank=True)
    birth_month = models.IntegerField(blank=True)
    birth_day = models.IntegerField(blank=True)
    channel = models.CharField(max_length=100)
    referral_code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# 이메일인증 smtp
class EmailConfirm(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='email_confirm',
        on_delete=models.CASCADE,
    )
    key = models.CharField(max_length=60)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)