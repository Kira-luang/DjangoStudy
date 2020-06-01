from time import sleep

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page


@cache_page(10)
def get_cache(request):
    print(111111111111111111111)
    sleep(5)
    return HttpResponse("测试缓存")


def my_cache(request):
    resault = cache.get('responses')
    if resault:
        return HttpResponse(resault)
    sleep(3)
    context = {'name': 'kira'}
    responses = render(request , 'mycache.html' , context=context)
    cache.set('responses' , responses)
    return responses
