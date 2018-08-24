from django.contrib import admin
from .models import Type, Cart_for_Subscription

# Register your models here.


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['type', 'type_str', 'component', 'detail', 'price', 'price_before']

@admin.register(Cart_for_Subscription)
class Cart_for_SubscriptionAdmin(admin.ModelAdmin):
  list_display = ['user', 'type_str', 'type', 'delivery_period', 'number', 'component', 'price']