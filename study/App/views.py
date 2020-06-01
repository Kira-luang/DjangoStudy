from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Image


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        name = request.POST.get('username')
        image = request.FILES.get('image')
        case = Image(name=name, os_path=image)
        case.save()
        return HttpResponse('{}注册成功'.format(case.name))


def show_image(request):
    name = request.GET.get('name')
    case = Image.objects.get(name=name)
    path = '/static/img/' + str(case.os_path)
    context = {
        'name': name,
        'path': path
    }
    return render(request, 'show.html', context=context)
