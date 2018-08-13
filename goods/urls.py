#good/urls
from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns=[

    path('',views.goods_list),
    path('<int:pk>',views.goods_detail),

]
