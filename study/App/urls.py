from django.contrib import admin
from django.urls import path, include, re_path

from App import views

urlpatterns = [
    re_path('register/', views.register, name='register'),
    re_path('hello/', views.hello, name='hello'),
]
