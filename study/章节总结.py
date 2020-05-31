# 模型继承
'''
如果是默认继承,便会在数据库中生成一个父表,子表会共用其字段(会产生关系) -> 详情看例子,无论addcat/adddog,id会叠加
要不在数据库中生成表,只是为了属性复用则需添加:
class Meta:
    abstract = True

关系型数据库,关系越复杂，效率越低
'''

# 额外知识:企业开发
'''
models -> sql(由模型映射到数据库)
sql -> models(由数据库映射到模型)
python manage.py inspectdb > App/models.py  (前提是要连接到数据库,会把某个数据库的表都映射过来)
> App/models.py 意思是生成到App/models.py,默认会生成在init文件里

里面的Meta会有manage=False,有这属性就不会再在数据库生成 -> 平常需要也能使用
'''
