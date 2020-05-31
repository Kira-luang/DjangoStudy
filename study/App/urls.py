from django.contrib import admin
from django.urls import path, re_path, include

from App import views

urlpatterns = [
    re_path('delwomen/', views.delwomen),
    re_path('delman/', views.delman),
    re_path('getman/', views.getman),
    re_path('getwoman/', views.getwoman),
]
