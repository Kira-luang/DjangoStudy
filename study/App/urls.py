from django.contrib import admin
from django.urls import path , include

from App import views

urlpatterns = [
    path('hello/' , views.hello) ,
]
