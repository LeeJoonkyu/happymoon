from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'login'

urlpatterns = [
    path('create/', views.information_create_view, name="rere"),
    path('join_success/', views.join_success, name="join_success"),
    path('loginone/', views.signin),
    path('loginsuccess/', views.loginsuccess, name="login"),
    path('logout/', auth_views.logout, name='logout', kwargs={'next_page': '/'}),
    ]

