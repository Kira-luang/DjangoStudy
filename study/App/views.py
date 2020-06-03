from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from App.models import Blog


@csrf_exempt
def edit_blog(request):
    if request.method == 'GET':
        return render(request , 'blog.html')
    elif request.method == 'POST':
        content = request.POST.get('text')
        print(content)
        blog = Blog(b_content=content)
        blog.save()
        return HttpResponse(content=blog.b_content)
