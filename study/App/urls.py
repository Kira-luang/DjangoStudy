from django.contrib import admin
from django.urls import path, include, re_path

from App import views

urlpatterns = [
    re_path('upload/', views.upload, name='upload'),
    re_path('register/', views.register),
]
