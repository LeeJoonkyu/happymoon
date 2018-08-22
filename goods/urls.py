#good/urls
from django.urls import path
from . import views

app_name = 'store_goods'

urlpatterns = [

    path('',views.goods_list, name='goods_list'),
    path('<int:pk>',views.goods_detail, name='goods_detail'),

]

