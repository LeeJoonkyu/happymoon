from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.information_create_view, name="signup"),
    path('join_success/', views.join_success, name="join_success"),
    path('login/', views.signin, name="login"),
    path('logout/', auth_views.logout, name='logout', kwargs={'next_page': '/accounts/login'}),
    ]

