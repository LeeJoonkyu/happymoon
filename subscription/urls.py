from django.urls import path, include
from . import views

app_name = 'subscription'

urlpatterns = [
    path('subscription/', views.subscription_list, name="subscription_list"),
    path('subscription_detail/HM-<str:str>/', views.subscription_detail, name="subscription_detail"),
]
