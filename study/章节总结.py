class Redis:
    '''能够利用内存进行缓存,比磁盘效率高很多'''
    pass


# 1.Redis安装

'''
Django并没有自带redis,所以要自行安装
pip install django-redis
pip install django-redis-cache
Windows自行下载一个Redis软件作为服务器
'''

# 2.Redis配置
'''
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
'''

# 3.Django多种缓存的应用
'''
设置
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache',  # 缓存表的名字
        'TIMEOUT': 60*5,  # 设置时间
    },
    "redis": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }

使用:
方法1:
@cache_page(10, cache='default') -> 10为时间,"cache="选择缓存
比较便捷

方法2:
cache.set('name', 'kira')
cache.get('name')
更加灵活
'''
