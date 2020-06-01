from time import sleep

from django.core.cache import caches , cache
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page


@cache_page(10 , cache='default')
def hello(request):
    sleep(5)
    return HttpResponse('Hello')


def redis(request):
    cache = caches['redis']
    if cache.get('name'):
        return HttpResponse('正在使用cache')
    sleep(5)
    cache.set('name' , 'kira')
    return HttpResponse('第一次')
