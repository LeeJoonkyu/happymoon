from django.contrib import admin
from .models import Goods, Cart_for_Goods

# Register your models here.
@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
  list_display = ['name','price']

@admin.register(Cart_for_Goods)
class Cart_for_GoodsAdmin(admin.ModelAdmin):
  list_display = ['goods','order']

