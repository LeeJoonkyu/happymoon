from django.db import models

# Create your models here.
class Product(models.Model):
  img_front = models.ImageField(upload_to = 'store/', blank=True)
  img_back = models.ImageField(upload_to = 'store/', blank=True)
  img_inner = models.ImageField(upload_to = 'store/', blank=True)
  img_side = models.ImageField(upload_to = 'store/', blank=True)
  name = models.CharField(max_length=20)
  price = models.IntegerField()
  detail = models.TextField()
  volume = models.IntegerField()
  size = models.IntegerField()
  manufac_date = models.CharField(max_length=30)
  useby_date = models.CharField(max_length=30)
  quantity = models.IntegerField()
  ingre = models.TextField()

  order = models.IntegerField()