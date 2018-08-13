from django.contrib import admin
from .models import Type

# Register your models here.


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['type', 'type_str', 'component', 'detail', 'price', 'price_before']
