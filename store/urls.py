from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='pad_list'),
    path('<int:pk>/', views.product_detail, name='pad_detail'),
]