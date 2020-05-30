class CSRF:
    '''对用户输入进行监控,防跨站攻击'''
    pass

# 跨站攻击
'''
利用用户输入,写入javascript脚本,然后会被Web服务器编译展现出来
'''

# CSRF怎么得到token
'''
{% csrf_token %}
'''

# CSRF的作用
'''
用户每一次POST,都会进行cookie的验证
只能POST到添加了{% csrf_token %}的页面
'''

# 课外知识:算法(了解就好)
'''
算法分多种
编码和解码:常见的是:Base64和urlencode
摘要算法/指纹算法/杂凑算法:SHA和MD5(默认128位二进制组成可转变成32为16进制的unicode)
加密:分为对称加密(DES,AES)和非对称加密(RSA,PGP)
'''
