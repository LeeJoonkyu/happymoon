from django.urls import path
from . import views

app_name = 'mypage'

urlpatterns = [
    path('', views.mypage),
    path('store_list/', views.store_list, name='store_list'),
]