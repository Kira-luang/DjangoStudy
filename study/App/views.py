from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Man, Women


def delwomen(request):
    entity = Women.objects.last()
    entity.delete()
    return HttpResponse('删除成功')


def delman(requets):
    entity = Man.objects.last()
    entity.delete()
    return HttpResponse('删除成功')


def getman(request):
    woman = Women.objects.last()
    return HttpResponse('{}'.format(woman.husband.name))


def getwoman(request):
    man = Man.objects.last()
    return HttpResponse('{}'.format(man.women.name))