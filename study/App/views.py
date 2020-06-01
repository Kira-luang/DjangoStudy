from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def upload(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        file = request.FILES.get('file')
        print(file)
        with open(r'E:\Pythonstudy\DjangoStudy\study\static\img\test.txt', 'wb') as f:
            for content in file.chunks():
                print(content)
                f.write(content)
                f.flush()
        return HttpResponse('上传成功')


def register(request):
    return render(request, 'register.html')
