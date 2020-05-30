from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def login(request):
    return render(request, 'login.html')


def show(request):
    username = request.POST.get('username')
    request.session['username'] = username  # 把cookie作为session_key,kv值作为data,传入数据库
    return render(request, 'show.html', context={'username': username})


def check(request):
    return HttpResponse('{}'.format(request.session.get('username')))


def exit(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('app:login'))
