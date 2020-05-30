from django.urls import path, include, re_path

from App import views

urlpatterns = [
    re_path('^login/', views.login, name='login'),
    re_path('^show/', views.show, name='show'),
    re_path('^check/', views.check, name='check'),
    re_path('^exit/', views.exit, name='exit'),
]