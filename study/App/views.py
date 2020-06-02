from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def hello(request):
    if request.method == 'GET':
        return render(request , 'hello.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse('Hello {}'.format(name))
