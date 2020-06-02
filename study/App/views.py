from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Student


def testpage(request):
    page = int(request.GET.get('page' , 1))
    per_page = int(request.GET.get('per_page' , 10))
    students = Student.objects.all()
    paginator = Paginator(students , per_page)
    page = paginator.page(page)
    context = {'paginator': paginator , 'page': page}
    return render(request , 'testpage.html' , context=context)


def add_student(request):
    for i in range(50):
        student = Student()
        student.name = 'kira{}'.format(i)
        student.save()
    return HttpResponse('添加成功')
