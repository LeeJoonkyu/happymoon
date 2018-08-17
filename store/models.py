from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Product(models.Model):
    img_front = models.ImageField(upload_to = 'store/', blank=True)
    img_back = models.ImageField(upload_to = 'store/', blank=True)
    img_inner = models.ImageField(upload_to = 'store/', blank=True)
    img_side = models.ImageField(upload_to = 'store/', blank=True)
    # p_code = models.IntegerField(blank=True)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    detail = models.TextField()
    volume = models.IntegerField()
    size = models.IntegerField()
    manufac_date = models.CharField(max_length=30)
    useby_date = models.CharField(max_length=30)
    quantity = models.IntegerField()
    ingre = models.TextField()

    def __str__(self):
        return self.name

#   order = models.OneToOneField('store.Cart')

class Cart_for_Pad(models.Model):
    user  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.IntegerField()
