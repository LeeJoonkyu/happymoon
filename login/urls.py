from django.urls import path
<<<<<<< HEAD
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('create/', views.information_create_view, name="rere"),
    path('join_success/', views.join_success, name="join_success"),
    path('loginone/', views.signin),
    path('loginsuccess/', views.loginsuccess, name="login"),
    path('logout/', auth_views.logout, name='logout', kwargs={'next_page': '/'}),
    ]
=======
from . import views

urlpatterns = [

    path('', views.login_detail),
]
>>>>>>> 7f5d1551887abe6fb3e1badd8233aae6a2a164d5
