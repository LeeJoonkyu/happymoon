from django.urls import path
from cart_subscription import views

app_name = 'cart_subscription'

urlpatterns = [
    path('', views.cart_subscription, name='cart_subscription'),
    path('payment/<str:merchant_uid>', views.payment, name='payment'),
    path('payment/pay_success/', views.pay_success, name='pay_success'),
]