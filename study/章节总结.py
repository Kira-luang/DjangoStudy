class DatabaseCache:
    '''下面的cache都建立在数据库磁盘上的,效率会比较低'''
    pass


# 1.建立缓存(直接用模块)
'''
第一步
设置缓存表(settings):
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache',  # 缓存表的名字
        'TIMEOUT': 60*5,  # 设置时间
    }
}

第二步
先在数据库建立缓存表 -> python manage.py createcachetable

第三步
在需要用缓存的函数中加上装饰器:
from django.views.decorators.cache import cache_page
@cache_page -> 可以重新设置时间
'''

# 2.自制缓存
'''
操作与字典神似
from django.core.cache import cache
resault = cache.get('responses')
cache.set('responses', responses)
'''
