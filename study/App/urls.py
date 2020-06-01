from django.contrib import admin
from django.urls import path , include

from App import views

urlpatterns = [
    path('cache/' , views.get_cache) ,
    path('mycache/' , views.my_cache) ,
]
