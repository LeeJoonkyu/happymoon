from django.contrib import admin
from .models import Information, EmailConfirm

@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ['name','email']


admin.site.register(EmailConfirm)