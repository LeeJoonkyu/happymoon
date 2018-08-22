from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Type(models.Model):
    img = models.ImageField()
    type_str = models.CharField(max_length=20, null=True)
    type = models.CharField(max_length=20)
    component = models.CharField(max_length=100)
    detail = models.TextField()
    price = models.IntegerField()
    price_before = models.IntegerField(null=True)

    def __str__(self):
        return self.type


class Cart_for_Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type_str = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    first_date = models.CharField(max_length=100, null=True)
    delivery_period = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=100)
    component = models.CharField(max_length=100)
    price = models.IntegerField()


