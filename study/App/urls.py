from django.contrib import admin
from django.urls import path , include

from App import views

urlpatterns = [
    path('login/' , views.login , name='login') ,
    path('getcode/' , views.getcode , name='getcode') ,
    path('strongcode/' , views.strong_code , name='strongcode') ,
    path('validate/' , views.validate , name='validate') ,
]
