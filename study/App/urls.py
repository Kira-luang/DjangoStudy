from django.contrib import admin
from django.urls import path, include, re_path
from App import views

urlpatterns = [
    path('', views.hello, name='hello'),
    re_path('^register/', views.register, name='register'),
    re_path('^solve/', views.solve, name='solve'),
    re_path('^login/', views.login, name='login'),
    re_path('^confirm/', views.confirm, name='confirm'),
    re_path('^json/', views.jsonify, name='json'),
]