from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'register.html')


def hello(request):
    return render(request, 'hello.html')
