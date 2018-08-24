from django.contrib import admin
from .models import Order_Subscription

# Register your models here.
@admin.register(Order_Subscription)
class Order_SubscriptionAdmin(admin.ModelAdmin):
  list_display = ['name', 'amount', 'merchant_uid']