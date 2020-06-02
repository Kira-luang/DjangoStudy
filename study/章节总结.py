class Paginator:
    '''分页器'''
    pass


# 1.url设置技巧
'''
li><a href="{% url 'app:testpage' %}?page={{ foo }}"> {{ foo }}</a></li>

Tip:?page={{ foo }}一定要加在{}外面
'''

# 2.分页器的使用
'''
paginator = Paginator(Student.objects.all(), per_page)
paginator.page(page): 参数page是第几页;paginator.page->展示per_page个Student的对象

'''
