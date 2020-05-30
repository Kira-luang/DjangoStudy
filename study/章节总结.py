class Session:
    '''是服务器识别用户的一种方法,可支持中文,自带使用salt和Base64'''
    pass

# Session重点知识
'''
request.session['username'] = username
Session建立时,会先到数据库存储,然后数据库会返回一个session_key.
这个session_key会作为cookie一部分response到服务器(cookie是其载体)
数据库的session_key == cookie里的sessionid
'''

# 应用
'''
建立session: request.session['username'] = username
获取session: request.session.get('username')
删除session: del request.session['username'] -> 会留下垃圾数据,不推荐
删除cookie: response.delete_cookie('sessionid') -> 会留下垃圾数据,不推荐
删除session+cookie: request.session.flush() -> 可直接清理数据库(最佳方法)
'''

# 遇到的坑
'''
1.由于session信息是存储在Django数据库的session中,所以必须要连接数据库才行

'''

# 额外知识
'''
以“=”号结束的,很可能是Base64编码的
'''
