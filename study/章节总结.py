class Model:
    pass

# 1.一对一的应用场景(依然是外键)
'''
场景一:
当一张表有多个字段时,对其进行拆分,变成两个表
场景二:
一个人对应一个身份证(如此之类)
'''

# 2.一对一应用与特性
'''
特性:
应用: 第一步A.a = OneToOneField('B'),制定A.a级联B。第二步需要建立一个函数去把A的某个记录去绑定B的某个记录

1.被申明的字段,被唯一键约束,所以产生1对1关系

2.当A的某个记录OneToOneField字段所绑定的对象B被删除,A的该记录也会被删除 -> 反之,A表不会变动
所以A是从表,B是主表
models.OneToOneField() == models.ForeignKey(unique=True, on_delete=models.CASCADE, related_name=a)

Tip:开发中往往要设置参数on_delete=models.PROTECT,以免数据误操作 -> 删除对象B时会受约束
models.OneToOneField(on_delete=models.PROTECT) == models.ForeignKey(unique=True, on_delete=models.PROTECT)


'''

# 3.on_delete设置介绍
'''
A.a = OneToOneField('B')
on_delete=models.CASCADE: 当B被删除时,A也会删除;A删除时,B不变
on_delete=models.PROTECT: 当B删除时,会报错.要先把A删除才能删B
on_delete=models.SET: A,B表删除互不干涉 -> 1.SET_NULL(允许NULL)和SET_DEFAULT(默认值)
'''


