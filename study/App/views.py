import random
from io import BytesIO

from PIL import Image , ImageDraw , ImageFont
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from study import settings


def login(request):
    if request.method == 'GET':
        return render(request , 'login.html')
    elif request.method == 'POST':
        pass


def getcode(request):
    mode = 'RGB'
    size = (200 , 120)
    red = 255
    green = 0
    blue = 0
    color = (red , green , blue)  # RGB默认三色素:红,绿,蓝
    canvas = Image.new(mode , size , color)
    image_draw = ImageDraw.ImageDraw(im=canvas , mode=mode)
    image_draw.text(xy=(0 , 0) , text='test')
    buffer = BytesIO()
    canvas.save(buffer , 'png')
    return HttpResponse(buffer.getvalue() , content_type='image/png')


# 加强验证码功能
def text():
    string = ''
    total = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    for _ in range(4):
        string += random.choice(total)
    return string


def background():
    number = random.randint(1 , 256)
    return number


def strong_code(request):
    canvas = Image.new(mode='RGB' , size=(150 , 100) , color=(background() , background() , background()))
    image_draw = ImageDraw.ImageDraw(im=canvas , mode='RGB')
    image_font = ImageFont.truetype(settings.FONT , size=random.randint(20 , 50))
    context = text()
    request.session['context'] = context
    image_draw.text(xy=(0 , 0) , text=context , font=image_font , fill=(background() , background() , background()))
    for i in range(5000):
        image_draw.point(xy=(random.randint(1 , 151) , random.randint(1 , 100)) ,
                         fill=(background() , background() , background()))
    buffer = BytesIO()
    canvas.save(buffer , 'png')
    return HttpResponse(buffer.getvalue() , content_type='image/png')


@csrf_exempt
def validate(request):
    code = request.POST.get('code')
    username = request.POST.get('username')
    context = request.session.get('context')
    print(code , context , username)
    if context == code:
        return HttpResponse('登陆成功')
    else:
        return HttpResponse('验证码出错')
