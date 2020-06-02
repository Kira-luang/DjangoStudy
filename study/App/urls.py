from django.contrib import admin
from django.urls import path , include

from App import views

urlpatterns = [
    path('admin/' , admin.site.urls) ,
    path('hello/' , views.hello) ,
    path('getmoney/' , views.getmoney) ,
]
