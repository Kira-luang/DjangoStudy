from django.contrib import admin
from django.urls import path , include , re_path

from App import views

urlpatterns = [
    re_path('hello/' , views.hello) ,
    re_path('redis/' , views.redis) ,
]
