from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Item, Student


def getstudent(request):
    item = Item.objects.first()
    allstudent = [x.name for x in item.student_set.all()]
    return HttpResponse(allstudent)


def getitem(request):
    student = Student.objects.first()
    return HttpResponse('{}'.format(student.item.name))
