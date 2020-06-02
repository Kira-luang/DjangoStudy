import random


class AOP:
    '''面向切面过程,中间件概念,作用就是拦截器'''
    pass


# 1.中间件出现的位置与名字
'''
执行1:Browser->urls->views->models->databases->views->templates->response
执行2:Browser->urls->views->templates->response

process_request:在urls->views
'''

# 2.AOP实现过程
'''
在项目里创建中间件的目录,在目录下创建一个py文件
在该py文件上创建中间件模型 -> class MiddleWare(MiddlewareMixin):
在设置上添加中间件的路劲 -> MIDDLEWARE=["middleware.ware.MiddleWare"]
'''

# 3.中间件应用场景/作用
'''
统计功能:获取/记录IP(浏览器)
权重选择:黑/白名单
实现反爬:搜索频率控制
'''
