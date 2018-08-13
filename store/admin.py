from django.contrib import admin
from .models import Product, Cart_for_Pad

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['name','price']

@admin.register(Cart_for_Pad)
class Cart_for_PadAdmin(admin.ModelAdmin):
  list_display = ['product','order']

