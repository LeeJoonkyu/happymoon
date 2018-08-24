#notice_list/urls.py


from django.urls import path
from . import views
app_name = 'notice_list'

urlpatterns = [

    path('', views.notice_list, name='notice_list'),
    path('notice_detail/<int:pk>', views.notice_detail, name='notice_detail'),

    # path('<int:pk>', views.notice_list, name = 'notice_list')
    # path('/notice_create', views.notice_create, name='notice_create'),

]