# 一对多就是传统的外键ForeignKey
'''
外键设置回顾
从获取主:直接通过ForeignKey的字段就能访问到主
主获取从:通过classname_set.all()获取全部 -> 一定要加all()要不然返回的是None

ForeignKey的related_name参数,只是更换了classname_set的名字而已,其他没变

一对多的ForeignKey要设置在多的那个记录上
'''
