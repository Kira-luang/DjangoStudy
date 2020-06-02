import datetime
import random


class AOP:
    '''面向切面过程,中间件概念,作用就是拦截器'''
    pass


# 1.中间件出现的位置与名字
'''
执行1:Browser->urls->views->models->databases->views->templates->response
执行2:Browser->urls->views->templates->response

process_request(self,request):在执行views的时候被调用
process_views(self,request,view_func,view_args,view_kwargs):在执行views之前被调用,也就是urls->views的过程
process_template_response(self,request,response):views执行完后调用
process_response(self,request,response):所有response返回浏览器之前
process_exception(self, request, exception):全web过程错误捕捉处理
'''

# 什么是跨域处理
'''
process_response应用场景
跨域处理:当IP+端口不一致时,就是跨域
实现跨域:在客户端伪装；服务器端添加属性,能允许所有域名访问

统一处理:对response进行统一处理的时候
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

# 4.cache的加强认识(每分钟只能搜索10次)
'''

'''
