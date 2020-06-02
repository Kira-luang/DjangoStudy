# 1.针对csrf的补充说明(深入了解)
'''
观察CsrfViewMiddleware源代码,会有不同的情况才能进行放行
第一种:
分析process_request -> request里只要有CSRF_COOKIE属性才能放行
所以要先获取CSRF_COOKIE -> {% csrf_token %}

第二种:
分析process_view(执行views前) -> if getattr(request, 'csrf_processing_done', False)
只要request里有csrf_processing_done的属性就能放行
内部没有提供,只能自己继承MiddlewareMixin,然后给request手动添加该属性

第三种:
分析process_view -> if getattr(callback, 'csrf_exempt', False)
csrf_exempt直接用来做views函数的装饰器,该函数就可以放行 -> @csrf_exempt

由此可见Csrf先在执行views前验证,在执行views过程中也会验证一次,任意一项通过后process_response就能正常返回
'''

# 2.中间件
'''
如果中间件设置了两个,并且都有process_view时
两个process_view会按顺序执行,如果第一个有返回值,就不会执行下一个中间件
'''
