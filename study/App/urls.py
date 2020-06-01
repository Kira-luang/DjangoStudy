from django.contrib import admin
from django.urls import path, include, re_path

from App import views

urlpatterns = [
    re_path('register/', views.register),
    re_path('show/', views.show_image),
]
