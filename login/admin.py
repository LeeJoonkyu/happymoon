from django.contrib import admin
<<<<<<< HEAD
from .models import Information


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
  list_display = ['name','email']
=======

# Register your models here.
>>>>>>> 7f5d1551887abe6fb3e1badd8233aae6a2a164d5
