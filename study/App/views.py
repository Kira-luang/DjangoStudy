import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse('Hello')


def getmoney(request):
    if random.randrange(10) > 5:
        return HttpResponse('GetMoney')
    else:
        return HttpResponse('抢不到')


def error(request):
    s = '1' + 5
    return HttpResponse(s)
