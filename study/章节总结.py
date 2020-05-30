class Token:
    '''本质上是set_cookie,并在数据库存储'''
    pass

# cookie,session与Token对比
'''
cookie:使用简洁,服务器压力小,但是数据不安全
session:服务器要维护(清除)session, 相对安全
Token:拥有session所有优点,维护麻烦,但支持移动端(不再依赖浏览器)
'''

# 被屏蔽的是PC端的做法
'''
PC端浏览器是可以发送和保存cookie的,所以可依赖于cookie,也依赖于浏览器
移动端APP是没有浏览器,所以利用不了cookie。可以利用json,通讯之间使用json协议,只需要在json中添加Token,
在request的时候对Token进行验证即可
'''
