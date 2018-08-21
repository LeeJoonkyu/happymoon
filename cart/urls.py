from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart, name='cart'),
    path('payment/', views.payment, name='payment'),
    path('payment/pay_now/', views.pay_now, name='pay_now'),
]