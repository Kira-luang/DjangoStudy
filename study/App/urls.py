from django.contrib import admin
from django.urls import path , include

from App import views

urlpatterns = [
    path('testpage/' , views.testpage , name='testpage') ,
    path('addstudent/' , views.add_student) ,
]
