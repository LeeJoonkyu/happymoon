from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription_list),
    path('<int:pk>/', views.subscription_detail),

]
