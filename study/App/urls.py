from django.contrib import admin
from django.urls import path, include

from App import views

urlpatterns = [
    path('getstudent/', views.getstudent),
    path('getitem/', views.getitem),
]
