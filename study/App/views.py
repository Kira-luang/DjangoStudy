from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Cat, Dog


def addcat(request):
    cat = Cat(eat='fish')
    cat.save()
    return HttpResponse(cat.id)


def adddog(request):
    dog = Dog(legs=4)
    dog.save()
    return HttpResponse(dog.id)
