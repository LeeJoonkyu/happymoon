from django.db import models

# Create your models here.


class Type(models.Model):
    img = models.ImageField()
    type_str = models.CharField(max_length=20, null=True)
    type = models.CharField(max_length=20)
    component = models.TextField()
    detail = models.TextField()
    price = models.IntegerField()
    price_before = models.IntegerField(null=True)


# class Addition(models.Model):
#     img = models.ImageField()
#     type =
#     price =
#     component =


