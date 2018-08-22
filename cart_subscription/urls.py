from django.urls import path
from cart_subscription import views

app_name = 'cart_subscription'

urlpatterns = [
    path('', views.cart_subscription, name='cart_subscription'),
    # path('payment/', views.payment, name='payment'),
    # path('payment/pay_now/<str:merchant_uid>', views.pay_now, name='pay_now'),
    # path('payment/pay_complete/', views.pay_complete, name='pay_complete'),
]