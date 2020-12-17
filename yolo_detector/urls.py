from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login,  name='login'),
    path('logout', views.logout, name='logout'),
    path('detect', views.detect,  name='detect'),
    path('list', views.list,  name='list'),
    path('view', views.view,  name='view'),
    path('auto_delete', views.auto_delete,  name='auto_delete'),
]