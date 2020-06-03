# 1.富文本原理和应用场景
'''
主要应用场景:博客和贴吧的评论

原理:把html标签作为功能展现出来,点击提交后,是伴随着html标签一齐传入函数中
'''

# 2.富文本插件使用过程
'''
第一步:安装django-tinymce
pip install django-tinymce

第二步:配置settings文件
先在INSTALLED_APPS添加tinymce应用,然后添加默认配置

TINYMCE_DEFAULT_CONFIG={
    'theme': 'advanced',
    'width': 800,
    'height': 600
}

第三步:创建模型
class Blog(models.Model):
    b_content = HTMLField()
    
Tip:HTMLField由源码可看出,储存内容是大文本格式存储的

第四步:迁移
python manage.py makemigrations
python manage.py migrate


第五步:template模板html设置
{% load static %}  这个放在顶部

下面的放在head模块里
<script type="text/javascript" src="/static/tiny_mce/tiny_mce.js"></script>
    <script>
        tinyMCE.init({
            'mode':'textareas', 'theme':'advanced',
            'width':800, 'height':600,
        })
    </script>
    
这个放在body里:    
<form action="" method="post">
    <textarea name="" id="" cols="30" rows="10">

    </textarea>
</form>

Tip:修改一下action和name就可以使用
'''
