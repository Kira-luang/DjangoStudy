from django.contrib import admin
from django.urls import path, include, re_path

from App import views

urlpatterns = [
    re_path('^addgoods/(?P<userid>\d+)/(?P<goodid>\d+)', views.add_goods),
    re_path('^addcutomer/(?P<userid>\d+)/(?P<goodid>\d+)', views.add_customer),
    re_path('^movegoods/(?P<userid>\d+)/(?P<goodid>\d+)', views.remove_good),
]
