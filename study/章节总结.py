# 模板语言input常用参数作用大全
'''
type: file(文件) text(文本,字) submit(上传)-> 文件上传必须用这个,不能用button
name: 取名(传入参数的名字)
placeholder: 输入提醒
value: 名字
enctype: 编码格式/上传文件的形式
'''

# 上传file与text的区别
'''
上传file由于比text要大,必须要切成多个包才能上传
form里添加enctype="multipart/form-data" -> <form action="" enctype="multipart/form-data">
'''

# 简单接收上传文件并保存的模板
'''
<form action="{% url "app:upload" %}" method="post" enctype="multipart/form-data">
    <input type="file" name="file" >
    <input type="submit" value="上传">
</form>
'''

# 课外知识:静态资源与模板区别
'''
templates(模板):支持模板语法 -> 会经过加工
static(静态资源): 不支持模板语法 -> 效率会比templates要高
'''

# 静态资源应用
'''
创造静态资源的文件夹 -> static
然后添加到设置上
差异可看static例子
'''
