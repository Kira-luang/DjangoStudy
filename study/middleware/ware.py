import datetime
import random

from django.core.cache import cache
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MiddleWare(MiddlewareMixin):
    def process_request(self , request):
        # 统计功能
        print(request.META.get('REMOTE_ADDR'))
        # 权重选择
        if request.META.get('REMOTE_ADDR') == '127.0.0.1':
            if random.randrange(10) > 5:
                return HttpResponse('GetMoney')
        # 搜索频率控制
        print(cache.get('ip') , request.META.get('ip'))
        if cache.get('ip'):
            return HttpResponse('访问过于频繁')
        if request.path == '/app/hello/':
            cache.set('ip' , 'test' , timeout=5)
        # 搜索频率加强控制每分钟10次
        container = cache.get('time' , [])
        now = datetime.datetime.now()
        if container:
            while (now - container[-1]).total_seconds() > 20:
                container.pop()
        container.insert(0 , now)
        if len(container) > 10:
            return HttpResponse('请求频繁')
        cache.set('time' , container , timeout=60)
