from django.contrib import admin
from .models import Review, Review_Comment


# Register your models here.
@admin.register(Review)
class ReivewAdmin(admin.ModelAdmin):
    list_display = ['user', 'star', 'title']


@admin.register(Review_Comment)
class Review_CommentAdmin(admin.ModelAdmin):
    list_display = ['review', 'message']