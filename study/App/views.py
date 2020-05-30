from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import datetime

# Create your views here.
from django.urls import reverse

from App.models import User


def hello(request):
    return HttpResponse('Hello')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def solve(request):
    user = User()
    user.username = request.POST.get('username')
    try:
        User.objects.get(username=user.username)
        return HttpResponseRedirect(reverse('app:register'))
    except Exception as e:
        user.password = request.POST.get('password')
        user.token = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        user.save()
    return HttpResponse('注册成功')


def confirm(request):
    try:
        name = request.POST.get('username')
        entity = User.objects.get(username=name)
        if entity.password == request.POST.get('password'):
            # response = HttpResponseRedirect(reverse('app:hello'))
            # response.set_cookie('token', entity.token)
            # return response
            data = {
                'username': name,
                'status_code': 200,
                'token': entity.token
            }
            return JsonResponse(data=data)
        else:
            raise Exception
    except Exception as e:
        print(e)
        data = {
            'status_code': 800,
            'message': 'GG'
        }
        return JsonResponse(data=data)
        # return HttpResponseRedirect(reverse('app:register'))


'''即使是前后端分离,然而协议是Json,所以request也是Json形式的请求,也就是字典'''
def jsonify(request):
    entity = User.objects.get(token=request.GET.get('token'))
    data = {
        'status_code': 200,
        'name': entity.name,
    }
    return JsonResponse(data)
